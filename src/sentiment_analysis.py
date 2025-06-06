import pandas as pd
from transformers import pipeline
import os

def analyze_sentiment(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    # Load sentiment model
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    # Apply to reviews
    results = classifier(df["review"].tolist(), truncation=True)

    # Add sentiment columns
    df["sentiment_label"] = [res["label"] for res in results]
    df["sentiment_score"] = [res["score"] for res in results]

    df.to_csv(output_path, index=False)
    print(f"Saved sentiment results to {output_path}")
    return df
