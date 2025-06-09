import os
import pandas as pd
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # For consistent results

def is_english(text):
    try:
        if not isinstance(text, str):
            return False
        if len(text.strip().split()) < 4:  # Skip short reviews
            return False
        return detect(text.strip()) == "en"
    except:
        return False

def preprocess_bank_reviews(input_dir="../data", output_dir="../data/cleaned"):
    os.makedirs(output_dir, exist_ok=True)

    bank_files = {
        "Commercial Bank of Ethiopia": "commercial_bank_of_ethiopia_reviews.csv",
        "Bank of Abyssinia": "bank_of_abyssinia_reviews.csv",
        "Dashen Bank": "dashen_bank_reviews.csv"
    }

    combined_df = []

    for bank, filename in bank_files.items():
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".csv", "_clean.csv"))

        try:
            df = pd.read_csv(input_path)
            print(f" Loaded {len(df)} reviews for {bank}")

            # Drop duplicates and rows with missing reviews or ratings
            df.drop_duplicates(subset="review", inplace=True)
            df.dropna(subset=["review", "rating"], inplace=True)

            # Filter for English reviews only
            df["is_english"] = df["review"].astype(str).apply(is_english)
            df = df[df["is_english"]].drop(columns=["is_english"])

            print(f" {len(df)} English reviews retained after filtering")

            # Normalize date format
            df["date"] = pd.to_datetime(df["date"], errors='coerce').dt.date.astype(str)

            # Reorder and clean up columns
            df = df[["review", "rating", "date", "bank", "source"]]

            # Save cleaned individual file
            df.to_csv(output_path, index=False)
            print(f" Saved cleaned file: {output_path}")

            combined_df.append(df)

        except FileNotFoundError:
            print(f" File not found: {input_path}")

    # Combine all into one DataFrame and save
    if combined_df:
        all_reviews = pd.concat(combined_df, ignore_index=True)
        combined_path = os.path.join(output_dir, "all_banks_reviews_clean.csv")
        all_reviews.to_csv(combined_path, index=False)
        print(f"\n Combined cleaned dataset saved: {combined_path} ({len(all_reviews)} total English reviews)")
