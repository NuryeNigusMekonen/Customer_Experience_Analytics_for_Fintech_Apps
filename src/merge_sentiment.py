import pandas as pd
import os

def merge_sentiment_with_reviews(sentiment_path, output_path):
    df = pd.read_csv(sentiment_path)
    final_df = df[["review", "rating", "date", "bank", "sentiment_label", "sentiment_score"]]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)
    print(f" Merged sentiment with review data at: {output_path}")
    return final_df
