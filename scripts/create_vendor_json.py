import pandas as pd
import json
import os
import re

def extract_price(text):
    match = re.search(r'(\d{2,5})\s*ብር', text)
    if match:
        return int(match.group(1))
    return 0

# Load your CSV
df = pd.read_csv('data/preprocessed_data.csv')

# Drop empty/NaN messages
df = df[df['cleaned_message'].notna()]
df = df[df['cleaned_message'].str.strip() != ""]
df = df.reset_index(drop=True)

# Build posts with price entity in expected format
posts = []
for i, row in df.iterrows():
    text = row['cleaned_message']
    price = extract_price(text)
    post = {
        "id": i,
        "text": text,
        "views": 0,
        "date": row['Date'],
        "entities": [
            {"label": "B-PRICE", "text": f"{price}Br"}
        ] if price else []
    }
    posts.append(post)

# Save to JSON
os.makedirs('data/vendor_posts', exist_ok=True)
with open('data/vendor_posts/vendor1.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, indent=4, ensure_ascii=False)

print("✅ vendor1.json with prices created successfully!")
