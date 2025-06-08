import os
from google_play_scraper import reviews, Sort
import pandas as pd

def fetch_and_save_reviews(app_id, bank_name, max_count=600, save_dir="../data"):
    os.makedirs(save_dir, exist_ok=True)
    
    all_reviews = []
    continuation_token = None

    try:
        while len(all_reviews) < max_count:
            batch, continuation_token = reviews(
                app_id,
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=200,
                continuation_token=continuation_token
            )
            all_reviews.extend(batch)
            if not continuation_token:
                break

    except Exception as e:
        print(f"Error fetching reviews for {bank_name}: {e}")

    print(f"Fetched {len(all_reviews)} reviews for {bank_name} (Requested: {max_count})")

    data = [{
        'review': rev['content'],
        'rating': rev['score'],
        'date': rev['at'].date().isoformat(),
        'bank': bank_name,
        'source': 'Google Play'
    } for rev in all_reviews]

    df = pd.DataFrame(data)

    filename = f"{bank_name.lower().replace(' ', '_')}_reviews.csv"
    df.to_csv(os.path.join(save_dir, filename), index=False)
    print(f"Saved to {filename}")
