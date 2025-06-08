import pandas as pd
import re

def cluster_keywords_to_themes(input_path, output_path, theme_rules):
    df = pd.read_csv(input_path)
    themed_rows = []

    for _, row in df.iterrows():
        bank = row['bank']
        keywords = row['top_keywords'].split(", ")

        theme_clusters = {theme: [] for theme in theme_rules}

        for word in keywords:
            for theme, terms in theme_rules.items():
                if any(re.search(rf'\b{term}\b', word, re.IGNORECASE) for term in terms):
                    theme_clusters[theme].append(word)

        for theme, matched in theme_clusters.items():
            if matched:
                themed_rows.append({
                    "bank": bank,
                    "theme": theme,
                    "keywords": ", ".join(set(matched))
                })

    themed_df = pd.DataFrame(themed_rows)
    themed_df.to_csv(output_path, index=False)
    print(f" Clustered themes saved to {output_path}")
    return themed_df
