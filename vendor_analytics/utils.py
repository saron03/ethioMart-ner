# vendor_analytics/utils.py

import re

def clean_price(text):
    match = re.search(r"(\d[\d,\.]*)", text)
    if match:
        return float(match.group(1).replace(",", ""))
    return None
