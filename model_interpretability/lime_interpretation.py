import sys
import os
import numpy as np
from lime.lime_text import LimeTextExplainer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.ner_wrapper import NERModelWrapper

class LimeCompatibleWrapper:
    def __init__(self, ner_model_wrapper):
        self.model = ner_model_wrapper
        self.labels = list(self.model.model.config.id2label.values())

    def predict_proba(self, texts):
        if isinstance(texts, str):
            texts = [texts]  # Ensure input is a list
        all_probs = []
        for text in texts:
            entities = self.model.pipeline(text, aggregation_strategy="simple")
            probs = np.zeros(len(self.labels))
            for entity in entities:
                label = entity.get('entity_group', entity.get('entity', 'O'))
                score = entity.get('score', 0.0)
                if label in self.labels:
                    label_idx = self.labels.index(label)
                    probs[label_idx] = max(probs[label_idx], score)  # Use max score for each label
            # Normalize probabilities to sum to 1
            total = probs.sum() or 1.0
            probs = probs / total
            all_probs.append(probs)
        return np.array(all_probs)

# Initialize model wrapper
model_path = r"C:\Users\saron\OneDrive\Desktop\kifya\week4\ethioMart-ner\model_comparison\results_bert-base-multilingual-cased\checkpoint-9"
model_wrapper = NERModelWrapper(model_path)
lime_wrapper = LimeCompatibleWrapper(model_wrapper)

explainer = LimeTextExplainer(class_names=lime_wrapper.labels)

text = "Elon Musk founded SpaceX and co-founded Tesla."

# Explain for B-LOC (index 2) since B-CONTACT_INFO may not be relevant for this text
explanation = explainer.explain_instance(
    text,
    lime_wrapper.predict_proba,
    num_features=10,
    labels=[2]  # index 2 = 'B-LOC'
)

print("Available labels:", explanation.available_labels())
print("Explanation for B-LOC:", explanation.as_list(label=2))

# Save explanation as HTML for visualization
output_dir = r"C:\Users\saron\OneDrive\Desktop\kifya\week4\ethioMart-ner\outputs"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "lime_output.html"), "w", encoding="utf-8") as f:
    f.write(explanation.as_html())  # Remove label parameter
print("LIME visualization saved as lime_output.html in outputs directory")