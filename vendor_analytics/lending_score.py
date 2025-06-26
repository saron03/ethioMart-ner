# vendor_analytics/lending_score.py

def compute_lending_score(metrics, weights=None):
    weights = weights or {
        'avg_views': 0.5,
        'posting_frequency': 0.3,
        'avg_price': 0.2
    }
    score = (
        metrics['avg_views'] * weights['avg_views'] +
        metrics['posting_freq'] * weights['posting_frequency'] +
        metrics['avg_price'] * weights['avg_price']
    )
    return round(score, 2)
