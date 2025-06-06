import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Manually define clusters/themes
THEME_RULES = {
    "Login & Access": ["login", "password", "otp", "access", "pin", "account", "credentials"],
    "Performance & Speed": ["slow", "crash", "freeze", "lag", "performance", "loading", "stuck", "hang"],
    "User Interface": ["ui", "interface", "design", "navigation", "layout", "buttons", "display"],
    "Feature Requests": ["feature", "add", "option", "transfer", "update", "budget", "history", "notification"],
    "Customer Support": ["support", "help", "service", "contact", "response", "call", "email", "assist"]
}


def map_keywords_to_theme(keywords):
    theme_hits = {theme: [] for theme in THEME_RULES}
    
    for word in keywords:
        for theme, related_words in THEME_RULES.items():
            if any(re.search(rf"\b{related_word}\b", word, re.IGNORECASE) for related_word in related_words):
                theme_hits[theme].append(word)
                
    return {theme: ", ".join(words) for theme, words in theme_hits.items() if words}

def extract_and_cluster_themes(input_path, output_path, top_n=30):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)

    banks = df['bank'].unique()
    all_theme_data = []

    for bank in banks:
        reviews = df[df['bank'] == bank]['review'].dropna().astype(str).tolist()

        tfidf = TfidfVectorizer(stop_words='english', max_df=0.8)
        X = tfidf.fit_transform(reviews)
        scores = X.sum(axis=0).A1
        terms = tfidf.get_feature_names_out()

        top_indices = scores.argsort()[::-1][:top_n]
        top_keywords = [terms[i] for i in top_indices]

        clustered = map_keywords_to_theme(top_keywords)
        all_theme_data.append({
            "bank": bank,
            **clustered
        })

    result_df = pd.DataFrame(all_theme_data)
    result_df.to_csv(output_path, index=False)
    print(f"Saved clustered themes to {output_path}")
    return result_df
