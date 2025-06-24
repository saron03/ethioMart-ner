import os
import ast
import numpy as np
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
from transformers import DataCollatorForTokenClassification
from sklearn.metrics import precision_recall_fscore_support

# Load the CSVs as DataFrames
df_train = pd.read_csv("../data/train.csv")
df_val = pd.read_csv("../data/val.csv")

# Extract unique labels from a DataFrame column of stringified lists
def extract_unique_labels(df):
    all_tags = df["ner_tags"].apply(ast.literal_eval).explode().unique()
    return set(all_tags)

# Extract unique labels from both train and validation sets, merge and sort
train_labels = extract_unique_labels(df_train)
val_labels = extract_unique_labels(df_val)
all_labels = sorted(train_labels.union(val_labels))
print("Extracted labels:", all_labels)

# Create label mappings based on extracted labels
labels = all_labels
label2id = {l: i for i, l in enumerate(labels)}
id2label = {i: l for l, i in label2id.items()}

def load_data(path):
    df = pd.read_csv(path)
    
    # Convert string representations of lists into actual lists
    df["tokens"] = df["tokens"].apply(ast.literal_eval)
    df["ner_tags"] = df["ner_tags"].apply(ast.literal_eval)

    # Map string labels to ids using the extracted label2id
    df["ner_tags"] = df["ner_tags"].apply(lambda tags: [label2id[tag] for tag in tags])
    
    dataset = Dataset.from_pandas(df)
    return dataset

train_dataset = load_data("../data/train.csv")
val_dataset = load_data("../data/val.csv")

def tokenize_and_align_labels(example, tokenizer):
    tokenized_inputs = tokenizer(
        example["tokens"],
        truncation=True,
        is_split_into_words=True,
        padding="max_length",
        max_length=128,
    )

    word_ids = tokenized_inputs.word_ids()
    previous_word_idx = None
    label_ids = []
    labels = example["ner_tags"]

    for word_idx in word_ids:
        if word_idx is None:
            label_ids.append(-100)
        elif word_idx != previous_word_idx:
            label_ids.append(labels[word_idx])
        else:
            label_ids.append(labels[word_idx])
        previous_word_idx = word_idx

    tokenized_inputs["labels"] = label_ids
    return tokenized_inputs

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)

    true_labels = [
        [id2label[l] for l in label if l != -100] for label in labels
    ]
    true_preds = [
        [id2label[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(preds, labels)
    ]

    precision, recall, f1, _ = precision_recall_fscore_support(
        sum(true_labels, []), sum(true_preds, []), average="weighted"
    )
    return {"precision": precision, "recall": recall, "f1": f1}

def fine_tune_model(model_name, train_dataset, val_dataset):
    print(f"\nFine-tuning {model_name} ...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(
        model_name,
        num_labels=len(labels),
        id2label=id2label,
        label2id=label2id,
    )
    
    train_tokenized = train_dataset.map(lambda x: tokenize_and_align_labels(x, tokenizer), batched=False)
    val_tokenized = val_dataset.map(lambda x: tokenize_and_align_labels(x, tokenizer), batched=False)

    data_collator = DataCollatorForTokenClassification(tokenizer)
    
    training_args = TrainingArguments(
        output_dir=f"./results_{model_name.replace('/', '_')}",
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        logging_dir="./logs",
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_tokenized,
        eval_dataset=val_tokenized,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )
    
    trainer.train()
    metrics = trainer.evaluate()
    print(f"Metrics for {model_name}: {metrics}")
    return model, metrics

if __name__ == "__main__":
    models_to_compare = [
        "xlm-roberta-base",
        "distilbert-base-multilingual-cased",
        "bert-base-multilingual-cased",
    ]
    
    all_metrics = {}
    for model_name in models_to_compare:
        model, metrics = fine_tune_model(model_name, train_dataset, val_dataset)
        all_metrics[model_name] = metrics

    print("\n========== MODEL COMPARISON SUMMARY ==========")
    for model_name, metrics in all_metrics.items():
        print(f"\nModel: {model_name}")
        print(f"F1: {metrics['eval_f1']:.4f}")
        print(f"Precision: {metrics['eval_precision']:.4f}")
        print(f"Recall: {metrics['eval_recall']:.4f}")
        print("-" * 40)
