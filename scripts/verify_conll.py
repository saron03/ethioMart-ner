import re

def verify_conll(file_path='data/labeled_data.conll'):
      valid_labels = {
          'B-Product', 'I-Product', 'B-LOC', 'I-LOC', 'B-PRICE', 'I-PRICE',
          'B-DELIVERY_FEE', 'I-DELIVERY_FEE', 'B-CONTACT_INFO', 'I-CONTACT_INFO', 'O'
      }
      messages = []
      current_message = []
      invalid_lines = []
      line_number = 0

      with open(file_path, 'r', encoding='utf-8') as f:
          for line in f:
              line_number += 1
              line = line.strip()
              if line:
                  parts = line.split()
                  if len(parts) != 2:
                      invalid_lines.append((line_number, line, "Incorrect format"))
                  else:
                      token, label = parts
                      if label not in valid_labels:
                          invalid_lines.append((line_number, line, f"Invalid label: {label}"))
                      current_message.append((token, label))
              else:
                  if current_message:
                      messages.append(current_message)
                      current_message = []

      if current_message:
          messages.append(current_message)

      print(f"Total Messages: {len(messages)}")
      if not (30 <= len(messages) <= 50):
          print(f"Warning: Message count ({len(messages)}) is outside 30–50 range.")
      
      if invalid_lines:
          print("\nInvalid Lines:")
          for line_num, line, error in invalid_lines:
              print(f"Line {line_num}: {line} ({error})")
      else:
          print("No format or label errors found.")
      
      return messages

if __name__ == "__main__":
      verify_conll()