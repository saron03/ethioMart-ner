import pandas as pd

def tokenize_and_label(message):
      tokens = message.split()  # Space-based tokenization
      labels = []
      for token in tokens:
          if token in ['ልብስ', 'ጫማ', 'ቦርሳ', 'ቲሸርት', 'ማሽን']:  # Products
              labels.append('B-Product')
          elif token in ['ለቤት', 'ለልጆች', 'ለሴቶች']:  # Product modifiers
              labels.append('I-Product')
          elif token in ['ዋጋ', 'በ']:  # Price indicators
              labels.append('B-PRICE')
          elif token in ['100', '200', '500', '1000', '2000', 'ብር']:  # Price values
              labels.append('I-PRICE')
          elif token in ['አዲስ', 'ቦሌ', 'መገናኛ', 'ለገስ']:  # Locations
              labels.append('B-LOC')
          elif token in ['አበባ']:  # Location parts
              labels.append('I-LOC')
          elif token in ['ነፃ', 'መላኪያ']:  # Delivery fee
              if token == 'ነፃ':
                  labels.append('B-DELIVERY_FEE')
              else:
                  labels.append('I-DELIVERY_FEE')
          elif token.startswith('@') or token.startswith('09'):  # Contact info
              labels.append('B-CONTACT_INFO')
          else:
              labels.append('O')
      return list(zip(tokens, labels))

def save_conll(data, output_file='reports/labeled_data.conll'):
      with open(output_file, 'w', encoding='utf-8') as f:
          for message in data:
              token_labels = tokenize_and_label(message)
              for token, label in token_labels:
                  f.write(f"{token} {label}\n")
              f.write("\n")

if __name__ == "__main__":
      df = pd.read_csv('data/preprocessed_data.csv')
      messages = df['cleaned_message'].dropna().head(50).tolist()
      save_conll(messages)