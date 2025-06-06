from google_play_scraper import Sort, reviews
import pandas as pd
import os

def fetch_and_save_reviews(app_id, bank_name, count=800, save_dir="../data"):
    os.makedirs(save_dir, exist_ok=True)

    all_reviews = []
    continuation_token = None

    while len(all_reviews) < count:
        r, continuation_token = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )
        all_reviews.extend(r)
        if not continuation_token:
            break

    data = [{
        'review': rev['content'],
        'rating': rev['score'],
        'date': rev['at'].date().isoformat(),
        'bank': bank_name,
        'source': 'Google Play'
    } for rev in all_reviews[:count]]

    df = pd.DataFrame(data)

    # Save separately
    filename = f"{bank_name.lower().replace(' ', '_')}_reviews.csv"
    df.to_csv(os.path.join(save_dir, filename), index=False)
    print(f"Saved {len(df)} reviews for {bank_name} to {filename}")
