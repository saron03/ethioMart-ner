# vendor_analytics/analyze_vendor.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from vendor_analytics.vendor_metrics import (
    calculate_posting_frequency, average_views,
    top_post, average_price
)
from vendor_analytics.lending_score import compute_lending_score

def analyze_vendor(vendor_file):
    with open(vendor_file, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    metrics = {
        'posting_freq': calculate_posting_frequency(posts),
        'avg_views': average_views(posts),
        'avg_price': average_price(posts),
        'top_post': top_post(posts)
    }

    score = compute_lending_score(metrics)

    print(f"\n📊 Vendor Report — {vendor_file}")
    print("Posting Frequency:", metrics['posting_freq'])
    print("Average Views:", metrics['avg_views'])
    print("Average Price:", metrics['avg_price'])
    print("Top Post Product & Views:", metrics['top_post'])
    print("💰 Lending Score:", score)

    return metrics, score

if __name__ == "__main__":
    import sys
    analyze_vendor(sys.argv[1])  # pass e.g. data/vendor_posts/vendor1.json
