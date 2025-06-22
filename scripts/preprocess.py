import pandas as pd
import regex as re

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

def preprocess_data(input_file='data/telegram_data.xlsx', output_file='report/preprocessed_data.csv'):
    df = pd.read_excel(input_file)
    if 'Message' not in df.columns:
        raise ValueError("No 'Message' column found in the input file.")
    df['cleaned_message'] = df['Message'].apply(preprocess_text)
    df.to_csv(output_file, index=False, encoding='utf-8')
    return df

if __name__ == "__main__":
    preprocess_data()
