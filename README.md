# EthioMart NER: Amharic E-commerce Data Extractor

## Task 5: Model Interpretability — NER Project

This task focuses on explaining how a Named Entity Recognition (NER) model makes its predictions using two popular model interpretability tools: **SHAP (SHapley Additive exPlanations)** and **LIME (Local Interpretable Model-agnostic Explanations)**. The aim is to build transparency and trust in the system, especially when handling ambiguous or challenging text.

---

## Objectives

- Apply SHAP and LIME to interpret the model’s decision-making process.
- Analyze difficult or ambiguous sentences where the model may misidentify entities.
- Generate visual and written reports that highlight how the model arrives at predictions.
- Use insights to propose ways to improve the model.

---

## Tools & Libraries Used

- Python 3.x
- Hugging Face `transformers`
- `shap`
- `lime`
- `torch`
- `sklearn`
- `matplotlib`, `seaborn`

---

## How to Run

### 1. Analyze Difficult Cases
Run ambiguous text examples to identify where the model struggles:
```bash
python model_interpretability/difficult_cases_analysis.py
```

2. SHAP Interpretability
Visualize token contributions using SHAP:
```bash
python model_interpretability/shap_interpretation.py
``` 

3. LIME Interpretability
Generate interactive HTML visualizations using LIME:
```bash
python model_interpretability/lime_interpretation.py
```

- Outputs/visualizations are saved in the outputs/ directory.
