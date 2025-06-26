# EthioMart NER: Amharic E-commerce Data Extractor

A project to build an Amharic Named Entity Recognition (NER) system that extracts business-relevant information from Telegram e-commerce messages.

# Task 6: FinTech Vendor Scorecard for Micro-Lending

This module analyzes Telegram vendor posts to evaluate vendor activity, engagement, and business potential for micro-lending decisions.

## Overview

EthioMart aims to identify promising vendors to offer micro-loans. This script processes a vendor’s Telegram posts, extracting metrics from text and metadata to build a detailed vendor profile.

## Key Features

- **Posting Frequency:** Calculates average posts per week to assess vendor activity.
- **Average Views:** Measures customer engagement via average views per post.
- **Top Performing Post:** Identifies the post with highest views including product details and price.
- **Average Price Point:** Computes average product price using NER-extracted price entities.
- **Lending Score:** Combines the above metrics into a weighted score representing vendor lending potential.

## Usage

Run the analysis script with a vendor JSON file containing post data:

```bash
python vendor_analytics/analyze_vendor.py data/vendor_posts/vendor1.json
