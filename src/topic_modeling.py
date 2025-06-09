def map_themes_to_reviews(input_path, output_path, theme_output_path=None):
    from bertopic import BERTopic
    import pandas as pd
    import os

    df = pd.read_csv(input_path)
    all_dfs = []

    banks = df['bank'].unique()

    for bank in banks:
        bank_df = df[df['bank'] == bank].copy()
        reviews = bank_df['review'].dropna().astype(str).tolist()

        if len(reviews) < 10:
            print(f"Skipping {bank}: Not enough reviews")
            continue

        topic_model = BERTopic(language="english", calculate_probabilities=False)
        topics, _ = topic_model.fit_transform(reviews)

        # Get mapping of topic to keywords
        topic_info = topic_model.get_topic_info()
        topic_keywords = {
            row["Topic"]: [kw for kw, _ in topic_model.get_topic(row["Topic"])]
            for _, row in topic_info.iterrows() if row["Topic"] != -1
        }

        def classify_theme(keywords: list) -> str:
            keyword_str = " ".join(keywords).lower()
            rules = {
                "Login Issues": ["login", "register", "username", "pin", "access", "otp", "account"],
                "Performance & Speed": ["slow", "lag", "freeze", "hang", "crash", "speed", "loading"],
                "App Usability": ["easy", "use", "simple", "interface", "navigation", "friendly"],
                "Customer Support": ["support", "help", "contact", "assist", "call"],
                "Feature Requests": ["feature", "add", "option", "notification", "tools"],
                "Update Problems": ["update", "latest", "fix", "bug", "issue", "sync"]
            }
            for theme, triggers in rules.items():
                if any(term in keyword_str for term in triggers):
                    return theme
            return "Other"

        # Add topic ID
        bank_df["theme_id"] = topics
        bank_df["theme_name"] = bank_df["theme_id"].apply(
            lambda tid: classify_theme(topic_keywords.get(tid, []))
        )
        all_dfs.append(bank_df)

    final_df = pd.concat(all_dfs, ignore_index=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)
    print(f" Reviews mapped with themes saved at: {output_path}")

    if theme_output_path:
        # Save summary themes per bank
        theme_summary = final_df.groupby(["bank", "theme_id", "theme_name"]).size().reset_index(name="count")
        theme_summary.to_csv(theme_output_path, index=False)
        print(f" Theme summary saved at: {theme_output_path}")

    return final_df
