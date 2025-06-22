# EthioMart Amharic E-commerce Data Extractor - Task 1

## Overview

This branch, `task1-data-preprocessing`, contains the code and documentation for **Task 1: Data Ingestion and Preprocessing** of the EthioMart Amharic E-commerce Data Extractor project. The goal is to preprocess a provided Telegram dataset (`telegram_data.xlsx`) to prepare Amharic text for Named Entity Recognition (NER). This work is part of a larger effort to build a centralized platform for Telegram-based e-commerce in Ethiopia.

## Task 1: Data Ingestion and Preprocessing

### Objective

   **Ingest**: Use the provided `telegram_data.xlsx` file containing messages from Ethiopian e-commerce Telegram channels.

   **Preprocess**: Clean the Amharic text in the `Message` column by removing punctuation and normalizing spaces.
   
   **Output**: Save the preprocessed data as `data/preprocessed_data.csv` with a `cleaned_message` column.

### Provided Data

The `data` folder contains:

* `telegram_data.xlsx`: Messages with columns `Channel Title`, `Channel Username`, `ID`, `Message`, `Date`, `Media Path`.
* `channels_to_crawl.xlsx`: List of Telegram channels (not used, as data is provided).
* `labeled_telegram_product_price_location.txt`: Reference for labeling (used in Task 2).
* `telegram_scrapper.py`: Scraper script (not used).
* `photos/`: Product images (not used in Task 1).

### Implementation

* Script: **scripts/preprocess.py**

    * Reads `telegram_data.xlsx` using `pandas`.

    * Applies text preprocessing to the **Message** column:

        * Removes punctuation using **regex**.

        * Normalizes spaces.

    * Saves output to `data/preprocessed_data.csv`, retaining original columns and adding `cleaned_message`.


### Output

* `data/preprocessed_data.csv`: Contains original columns plus `cleaned_message` with cleaned Amharic text (e.g., “ልብስ ዋጋ 500 ብር” without punctuation).


## Setup Instructions

1. **Clone the Repository**:
```bash
git clone https://github.com/saron03/ethioMart-ner
cd ethioMart-ner
git checkout task1-data-preprocessing
```

2.  **Install Python**:

    * Ensure Python 3.8+ is installed: `python --version`.
    * Download from [python.org](https://www.python.org/downloads/) if needed.

3.  **Create Virtual Environment**:
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

4. **Install Dependencies**:
```
pip install pandas regex openpyxl
```

5. **Place Data**:
    * Ensure the `data` folder (with `telegram_data.xlsx`) is in the project root.
    * Note: `data/` is excluded from Git via `.gitignore` due to size/sensitivity.

6. **Run Preprocessing**:
```
python scripts/preprocess.py
```

* Outputs `data/preprocessed_data.csv`.

## File Structure

* **scripts/preprocess.py**: Preprocessing script.  
* **.gitignore**: Excludes `data/`, `venv/`, and temporary files.  
* **data/** (not committed):  
  * `telegram_data.xlsx`: Input data.  
* **report/**:
  * `preprocessed_data.csv`: Output data.
## Challenges

* **Amharic Text**: The fidäl script required careful preprocessing to preserve word boundaries.  
* **Column Verification**: Ensured the `Message` column was correctly identified in `telegram_data.xlsx`.

## Next Steps

* **Task 2**: Label 30–50 messages in CoNLL format (see `task2-data-labeling` branch).
* **Future Tasks**: Fine-tune NER models, compare performance, and apply interpretability tools.