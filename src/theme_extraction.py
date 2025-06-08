import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(input_path, output_path, top_n=50):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    banks = df["bank"].unique()
    results = []

    for bank in banks:
        reviews = df[df["bank"] == bank]["review"].dropna().astype(str).tolist()
        tfidf = TfidfVectorizer(stop_words='english', max_df=0.8)
        X = tfidf.fit_transform(reviews)
        scores = X.sum(axis=0).A1
        terms = tfidf.get_feature_names_out()
        top_indices = scores.argsort()[::-1][:top_n]
        top_keywords = [terms[i] for i in top_indices]

        results.append({
            "bank": bank,
            "top_keywords": ", ".join(top_keywords)
        })

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_path, index=False)
    print(f" Keyword output saved to {output_path}")
    return result_df