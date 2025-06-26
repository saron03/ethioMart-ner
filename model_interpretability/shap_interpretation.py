import shap
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.ner_wrapper import NERModelWrapper

# Initialize model wrapper
model_path = r"C:\Users\saron\OneDrive\Desktop\kifya\week4\ethioMart-ner\model_comparison\results_bert-base-multilingual-cased\checkpoint-9"
model_wrapper = NERModelWrapper(model_path)

# Example text input
text_samples = [
    "Barack Obama was born in Hawaii.",
    "Apple is looking at buying U.K. startup for $1 billion."
]

# Use SHAP with transformer models
explainer = shap.Explainer(model_wrapper.predict_proba, masker=shap.maskers.Text())

# Generate SHAP values
shap_values = explainer(text_samples)

# Save SHAP visualization as HTML
output_dir = r"C:\Users\saron\OneDrive\Desktop\kifya\week4\ethioMart-ner\outputs"
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
html_content = shap.plots.text(shap_values[0], display=False)  # Get HTML string
with open(os.path.join(output_dir, "shap_output_0.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print("SHAP visualization saved as shap_output_0.html in outputs directory")