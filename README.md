# Task 2 – Sentiment and Thematic Analysis for Fintech App Reviews

This project performs sentiment and thematic analysis on user reviews of Ethiopian bank mobile apps from the Google Play Store. It uses transformer-based models for sentiment classification and TF-IDF for keyword extraction, clustering those keywords into themes.

---

##  Task Summary

###  Goals
- Perform **sentiment classification** using BERT on user reviews.
- Extract significant **keywords** using TF-IDF per bank.
- **Cluster** those keywords into 3–5 broad, meaningful **themes** per bank.
- Save clean outputs for analysis and reporting.

---

##  Tools & Libraries
- `transformers` (Hugging Face) – BERT-based sentiment classification
- `sklearn` – TF-IDF vectorization
- `pandas`, `os` – Data manipulation & I/O
- Python 3.8+

---

##  Folder Structure

```

project-root/
├── data/
│   └── cleaned/all\_banks\_reviews\_clean.csv
├── outputs/
│   ├── sentiment/
│   │   ├── all\_banks\_sentiment.csv
│   │   ├── reviews\_with\_sentiment.csv
│   │   └── sentiment\_by\_bank\_and\_rating.csv
│   └── themes/
│       ├── bank\_keywords.csv
│       └── bank\_themes\_final.csv
├── src/
│   ├── sentiment\_analysis.py
│   ├── theme\_extraction.py
│   ├── theme\_clustering.py
│   └── merge\_sentiment.py
    └── cleaning.py
    └── scraping.py
└── notebook/
└── analysis.ipynb
└── scrap-and-save.ipynb

```

---

##  Outputs

| File | Description |
|------|-------------|
| `all_banks_sentiment.csv` | Sentiment predictions for each review |
| `reviews_with_sentiment.csv` | Merged review + sentiment data |
| `sentiment_by_bank_and_rating.csv` | Aggregated sentiment score by rating and bank |
| `bank_keywords.csv` | Top TF-IDF keywords per bank |
| `bank_themes_final.csv` | Manually grouped themes per bank using keyword clusters |

---

##  How to Run the Pipeline

1. Activate your virtual environment and install dependencies.
2. Run the notebook:
```

notebook/task\_2\_analysis.ipynb

```
3. Outputs will be saved under `outputs/sentiment/` and `outputs/themes/`.

---

##  Themes Defined (Rule-Based)
| Theme             | Sample Keywords |
|------------------|------------------|
| Login & Access   | login, password, otp, account |
| Performance      | slow, crash, freeze |
| UI/UX            | ui, design, layout |
| Feature Request  | feature, add, option |
| Customer Support | support, help, contact |

---

##  Status

Task 2 is fully completed:
- BERT-based sentiment analysis (English only)
- TF-IDF keyword extraction
- Rule-based theme grouping
- Modular scripts and final pipeline
```

