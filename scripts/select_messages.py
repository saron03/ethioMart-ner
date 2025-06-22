import pandas as pd

df = pd.read_csv('data/preprocessed_data.csv')
messages = df['cleaned_message'].dropna().head(50).tolist()
with open('data/selected_messages.txt', 'w', encoding='utf-8') as f:
    for i, msg in enumerate(messages, 1):
        f.write(f"Message {i}: {msg}\n")
print(f"Saved {len(messages)} messages to reports/selected_messages.txt")