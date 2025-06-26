import sys
import os
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.ner_wrapper import NERModelWrapper

# Initialize model wrapper
model_path = r"C:\Users\saron\OneDrive\Desktop\kifya\week4\ethioMart-ner\model_comparison\results_bert-base-multilingual-cased\checkpoint-9"
model_wrapper = NERModelWrapper(model_path)

# Ambiguous or tricky examples + control text
texts = [
    "I saw Washington flying to Paris. (Is 'Washington' a person or a place?)",
    "The Amazon workers are on strike. (Amazon the company or the river?)",
    "Jordan scored 30 points. (Michael Jordan or the country?)",
    "Contact us at +251-912-345678 in Addis Ababa for a 100 ETB product."
]

# Verify checkpoint files
print("\nVerifying model checkpoint files:")
checkpoint_dir = model_path
expected_files = ['config.json', 'pytorch_model.bin', 'tokenizer.json']
for f in expected_files:
    file_path = os.path.join(checkpoint_dir, f)
    print(f"{f}: {'Found' if os.path.exists(file_path) else 'Missing'}")

# Test raw model output
print("\nTesting raw model output (logits):")
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForTokenClassification.from_pretrained(model_path, local_files_only=True)
test_text = "Contact us at +251-912-345678 in Addis Ababa."
inputs = tokenizer(test_text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
logits = outputs.logits[0]  # Shape: (seq_len, num_labels)
predictions = torch.argmax(logits, dim=-1).numpy()
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
labels = [model.config.id2label[idx] for idx in predictions]
print("\nRaw model predictions for test text:")
for token, label in zip(tokens, labels):
    print(f"{token}: {label}")

# Analyze pipeline predictions
for text in texts:
    print(f"\nText: {text}")
    
    # Raw token-level predictions
    print("Raw predictions (token-level):")
    raw_predictions = model_wrapper.pipeline(text, aggregation_strategy=None)
    if not raw_predictions:
        print("No entities detected (raw).")
    else:
        for entity in raw_predictions:
            print(f"{entity['word']}: {entity['entity']} (score: {entity['score']:.4f})")
    
    # Grouped predictions
    print("\nGrouped entities:")
    grouped_predictions = model_wrapper.pipeline(text, aggregation_strategy="simple")
    if not grouped_predictions:
        print("No grouped entities detected.")
    else:
        for entity in grouped_predictions:
            print(f"{entity['word']}: {entity['entity_group']} (score: {entity})")
    
    # Tokenized input
    print("\nTokenized input:")
    tokens = model_wrapper.tokenizer.tokenize(text)
    print(tokens)