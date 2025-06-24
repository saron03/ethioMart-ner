# Task 3: Fine-Tuning NER Model for Amharic Telegram Messages

This task involves fine-tuning a Named Entity Recognition (NER) model to extract key entities such as product names, prices, and locations from Amharic Telegram e-commerce messages.

## Overview
- Utilized pre-trained transformer models such as XLM-Roberta, bert-tiny-amharic, and afroxmlr.
- Prepared and loaded labeled Amharic dataset in CoNLL format.
- Tokenized data and aligned entity labels with tokens.
- Fine-tuned models using Hugging Face Trainer API with GPU support.
- Evaluated model performance on validation set using metrics like F1-score, precision, and recall.
- Saved the fine-tuned model for future use.

## Dependencies
- `transformers`
- `datasets`
- `torch`
- `seqeval`
- `sklearn`

## Usage
Run the training script `train_ner.py` in a GPU-enabled environment (e.g., Google Colab).

