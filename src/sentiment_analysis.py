import pandas as pd
from transformers import pipeline
import os

def analyze_sentiment(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    sentiments = []
    scores = []

    for review in df["review"].astype(str):
        try:
            res = classifier(review[:512])[0]
            sentiments.append(res["label"])
            scores.append(res["score"])
        except Exception:
            sentiments.append("unknown")
            scores.append(0.0)

    df["sentiment_label"] = sentiments
    df["sentiment_score"] = scores

    df.to_csv(output_path, index=False)
    print(f" Sentiment saved to {output_path}")
    return df