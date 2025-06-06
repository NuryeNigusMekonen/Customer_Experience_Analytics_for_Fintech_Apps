import os
import pandas as pd

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
            print(f"Loaded {len(df)} reviews for {bank}")

            # Drop duplicates and rows with missing reviews or ratings
            df.drop_duplicates(subset="review", inplace=True)
            df.dropna(subset=["review", "rating"], inplace=True)

            # Normalize date format
            df["date"] = pd.to_datetime(df["date"], errors='coerce').dt.date.astype(str)

            # Reorder and clean up columns
            df = df[["review", "rating", "date", "bank", "source"]]

            # Save cleaned individual file
            df.to_csv(output_path, index=False)
            print(f"Cleaned and saved {len(df)} reviews to {output_path}")

            combined_df.append(df)

        except FileNotFoundError:
            print(f"File not found: {input_path}")

    # Combine all into one DataFrame and save
    if combined_df:
        all_reviews = pd.concat(combined_df, ignore_index=True)
        all_reviews.to_csv(os.path.join(output_dir, "all_banks_reviews_clean.csv"), index=False)
        print(f"\nCombined cleaned dataset saved: {len(all_reviews)} total reviews")

