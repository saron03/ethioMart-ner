# EthioMart Amharic E-commerce Data Extractor - Task 2

## Overview

This branch, `task2-data-labeling`, implements **Task 2: Labeling Data in CoNLL Format** for the EthioMart project. It labels 30–50 Amharic messages from Telegram e-commerce channels in CoNLL format for Named Entity Recognition (NER), identifying entities like Product, Price, Location, Delivery Fee, and Contact Info.

## Task 2: Labeling Data in CoNLL Format

### Objective

* Label 30–50 messages from `data/preprocessed_data.csv` ( `cleaned_message` column).
* Entities: Product, Price, Location, Delivery Fee, Contact Info.
* Save as `report_task2/labeled_data.conll`.

### Provided Data

* `data/preprocessed_data.csv`: Preprocessed messages from `data/telegram_data.xlsx` (Task 1).
* `data/labeled_telegram_product_price_location.txt`: Labeling reference.
* `data/telegram_data.xlsx`: Original messages ( `Message` column).
* `data/photos/`: Product images for context.
* `data/channels_to_crawl.xlsx`, `data/telegram_scrapper.py`: Not used.

### Implementation

### Script: `scripts/select_messages.py`

- Selects 50 messages from the `cleaned_message` column for labeling.
- Saves the output to `data/selected_messages.txt`.

### Script: `scripts/label_data.py`

- Tokenizes messages and applies rule-based labels (e.g., “ልብስ” → `B-Product`).
- Outputs labeled data in CoNLL format to `report_task2/labeled_data.conll`.

### Script: `scripts/verify_conll.py`

- Validates that the message count is between 30–50.
- Checks for proper CoNLL label format.

### Manual Verification

- Reviewed labels against `labeled_telegram_product_price_location.txt`.
- Corrected annotation errors (e.g., “ልብስ O” → `B-Product`).
- Ensured multi-word entities are labeled correctly (e.g., “አዲስ አበባ” → `B-LOC`, `I-LOC`).

## Output

* `report_task2/labeled_data.conll`: Contains 50 manually labeled messages with entities in CoNLL format.

**Entity Labels Used:**

- `B-Product`, `I-Product`: Products (e.g., “ልብስ”)
- `B-LOC`, `I-LOC`: Locations (e.g., “አዲስ አበባ”)
- `B-PRICE`, `I-PRICE`: Prices (e.g., “500 ብር”)
- `B-DELIVERY_FEE`, `I-DELIVERY_FEE`: Delivery fees (e.g., “ነፃ መላኪያ”)
- `B-CONTACT_INFO`, `I-CONTACT_INFO`: Contact info (e.g., “@ShopEthio”)
- `O`: Tokens outside named entities


## Setup Instructions

1.  **Clone Repository**:
```bash
git clone https://github.com/saron03/ethioMart-ner
cd ethioMart-ner
git checkout task2-data-labeling
```

2.  **Install Python**:

* Python 3.8+: `python --version`.
* Download from [python.org](https://www.python.org/downloads/).

3. **Create Virtual Environment**:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

4.  **Install Dependencies**:
```bash
pip install pandas regex openpyxl
```

5.  **Place Data**:

* Ensure `data/` contains `preprocessed_data.csv` and `report_task2/` contains `labeled_data.conll`, etc.

6. **Run Scripts**:

* Select messages:
```bash
python scripts/select_messages.py
```

* Generate labels:
```bash
python scripts/label_data.py
```

* Verify:
```bash
python scripts/verify_conll.py
```

## File Structure

* `scripts/select_messages.py`: Message selection.
* `scripts/label_data.py`: Labeling.
* `scripts/verify_conll.py`: Validation.
* `report_task2/labeled_data.conll`: Labeled output.
* `data/selected_messages.txt`: Selected messages.
* `.gitignore`: includes `data/`.

## Challenges

* **Amharic Tokenization**: Fidäl script required careful manual corrections.
* **Label Accuracy**: Ensured consistency with `labeled_telegram_product_price_location.txt`.
* **Optional Entities**: Included `DELIVERY_FEE` and `CONTACT_INFO`.

## Next Steps

*  **Interim Submission**: See `task-interim-submission` for PDF and deliverables.
*  **Future Tasks**: NER model fine-tuning, performance comparison.

## Submission

Task 1 ans Task 2 are part of interim submission due 23:00 EAT, June 22, 2025.