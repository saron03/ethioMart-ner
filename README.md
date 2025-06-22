# EthioMart NER: Amharic E-commerce Data Extractor

A project to build an Amharic Named Entity Recognition (NER) system that extracts business-relevant information from Telegram e-commerce messages.

## Goal

Help EthioMart centralize and analyze e-commerce activity by:

- Extracting entities like **Product**, **Price**, and **Location** from Amharic messages.
- Scoring vendors based on engagement and pricing to support **micro-lending** decisions.

## Key Components

- **Data Ingestion**: Collect messages from Telegram channels.
- **Preprocessing**: Clean and prepare Amharic text.
- **Labeling**: Manually tag 30–50 messages using CoNLL format.
- **Model Fine-tuning**: Train transformer models (e.g., XLM-R) on labeled data.
- **Evaluation**: Compare models using F1-score and explain predictions with SHAP/LIME.
- **Vendor Scorecard**: Rank vendors by activity, engagement, and pricing.

## Outputs

- `preprocessed_data.csv`: Cleaned messages
- `labeled_data.conll`: Labeled NER training data
- `fine-tuned model`: For extracting entities
- `vendor_scorecard.csv`: Vendor metrics and lending scores

## Timeline

- **Interim Submission**: 22 June 2025  
- **Final Submission**: 24 June 2025

---