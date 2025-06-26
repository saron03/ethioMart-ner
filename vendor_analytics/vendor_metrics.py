# vendor_analytics/vendor_metrics.py

import datetime
from collections import defaultdict
import numpy as np

def calculate_posting_frequency(posts):
    dates = [datetime.datetime.fromisoformat(p['date']) for p in posts]
    if len(dates) < 2:
        return 0
    duration_days = (max(dates) - min(dates)).days + 1
    weeks = duration_days / 7
    return round(len(posts) / weeks, 2)

def average_views(posts):
    views = [p.get('views', 0) for p in posts]
    return round(np.mean(views), 2) if views else 0

def top_post(posts):
    top = max(posts, key=lambda x: x.get('views', 0))
    return {
        'views': top.get('views'),
        'text': top.get('text', ''),
        'price': extract_price(top.get('entities', []))
    }

def extract_price(entities):
    prices = [float(e['text'].replace("Br", "").strip()) for e in entities if e['label'] == 'B-PRICE']
    return round(np.mean(prices), 2) if prices else 0

def average_price(posts):
    all_prices = []
    for post in posts:
        entities = post.get('entities', [])
        all_prices += [float(e['text'].replace("Br", "").strip()) for e in entities if e['label'] == 'B-PRICE']
    return round(np.mean(all_prices), 2) if all_prices else 0
