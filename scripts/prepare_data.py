import pandas as pd
from sklearn.model_selection import train_test_split

import os

print("Current directory:", os.getcwd())
print("File exists:", os.path.exists('data/labeled_data.conll'))


def read_conll(filepath):
    sentences = []
    labels = []
    with open(filepath, 'r', encoding='utf-8') as f:
        tokens = []
        ner_tags = []
        for line in f:
            line = line.strip()
            if not line:
                if tokens:
                    sentences.append(tokens)
                    labels.append(ner_tags)
                    tokens = []
                    ner_tags = []
            else:
                splits = line.split()
                tokens.append(splits[0])
                ner_tags.append(splits[1])
        # Catch last sentence
        if tokens:
            sentences.append(tokens)
            labels.append(ner_tags)
    return sentences, labels

sentences, labels = read_conll('data/labeled_data.conll')

# Split train and val
train_sents, val_sents, train_labels, val_labels = train_test_split(
    sentences, labels, test_size=0.2, random_state=42)

# Save as CSV with two columns: tokens and ner_tags (both stored as lists)
train_df = pd.DataFrame({'tokens': train_sents, 'ner_tags': train_labels})
val_df = pd.DataFrame({'tokens': val_sents, 'ner_tags': val_labels})

train_df.to_csv('data/train.csv', index=False)
val_df.to_csv('data/val.csv', index=False)
