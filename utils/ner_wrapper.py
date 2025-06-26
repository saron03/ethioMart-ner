from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import numpy as np

class NERModelWrapper:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
        self.model = AutoModelForTokenClassification.from_pretrained(model_path, local_files_only=True)
        print("Model labels (id2label):", self.model.config.id2label)
        self.pipeline = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple", device=-1)
        print(f"Device set to use {'cpu' if self.pipeline.device.type == 'cpu' else 'cuda'}")
        self.labels = self.model.config.id2label.values()

    def predict(self, text):
        result = self.pipeline(text)
        tokens = [ent['word'] for ent in result]
        labels = [ent['entity_group'] for ent in result]
        return {"tokens": tokens, "labels": labels}

    def predict_proba(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        predictions = []
        num_labels = len(self.pipeline.model.config.id2label)
        
        for text in texts:
            entities = self.pipeline(text)
            probs = np.zeros(num_labels)
            
            for entity in entities:
                label = entity.get('entity_group', entity.get('entity', 'O'))
                score = entity.get('score', 0.0)
                label_idx = None
                for k, v in self.pipeline.model.config.id2label.items():
                    if v == label:
                        label_idx = k
                        break
                if label_idx is None:
                    label_idx = [k for k, v in self.pipeline.model.config.id2label.items() if v == 'O'][0]
                probs[label_idx] = max(probs[label_idx], score)
            
            total = probs.sum() or 1.0
            probs = probs / total
            predictions.append(probs)
        
        return np.array(predictions)