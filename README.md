
#  Customer Experience Analytics for Fintech Apps

This project provides a full pipeline for analyzing user experience and sentiment in fintech mobile app reviews. It combines natural language processing (NLP), data visualization, and topic modeling to extract insights from multilingual (English + Amharic) reviews collected from app stores.

---

## Project Overview

This solution is part of a 10 Academy AI Mastery program. It includes:

-  **Task 1: Data Loading, Cleaning, and Exploration**
-  **Task 2: Sentiment Analysis**
-  **Task 3: Thematic Analysis using Topic Modeling**
-  **Task 4: Insights, Visualizations, and Ethical Considerations**

---

##  Folder Structure

```bash
├── data/                      # Original raw datasets
├── outputs/
│   ├── sentiment/             # Reviews with sentiment scores and labels
│   ├── themes/                # Thematic clustering outputs (topics/themes)
├── src/                       # Source code
│   ├── preprocessing.py       # Data cleaning and normalization
│   ├── sentiment_analysis.py  # Sentiment model and scoring
│   ├── topic_modeling.py      # BERTopic-based theme extraction
│   ├── utils.py               # Utility functions
├── notebooks/
│   ├── task_1_eda.ipynb
│   ├── task_2_sentiment.ipynb
│   ├── task_3_themes.ipynb
│   ├── task_4_insights.ipynb
├── README.md
````

---

##  Requirements

Python ≥ 3.10
Install dependencies with:

```bash
pip install -r requirements.txt
```

Key packages:

* `pandas`, `matplotlib`, `seaborn`
* `nltk`, `scikit-learn`
* `BERTopic`, `sentence-transformers`
* `wordcloud`, `unidecode`

---

##  Tasks Summary

###  Task 1: Data Preparation

* Cleaned raw app reviews.
* Standardized rating and language fields.
* Converted dates, normalized Amharic/English text.

###  Task 2: Sentiment Analysis

* Used a multilingual Transformer model to classify reviews into `POSITIVE` or `NEGATIVE`.
* Output: `reviews_with_sentiment.csv`

###  Task 3: Topic Modeling (Themes)

* Used `BERTopic` to group reviews into semantic themes (e.g., *Login Issues*, *App Usability*).
* Applied keyword-based rule mapping to label topics.
* Output: `bank_themes_bertopic.csv`, `reviews_with_themes.csv`

###  Task 4: Visual Insights & Ethics

*  Created charts for:

  * Sentiment over time
  * Review count by theme
  * Sentiment distribution by bank
  * Rating histograms
  * Theme × Sentiment heatmaps

*  Suggested Improvements:

  * Improve **login reliability**
  * Reduce **crash frequency**
  * Add features like **budget tracking**, **statements**
  * Simplify **user interface**

*  Ethical Notes:

  * Review bias exists (users write mostly when angry or excited).
  * Multilingual NLP challenges.
  * Class imbalance between negative/positive reviews.

---

## Sample Visuals

## Visualizations

### sentiment distribution
![sentiment distribution](outputs/visuals/sentiment_distribution.png)

### Rating distributions by bank
![Rating distributions by bank](outputs/visuals/rating_distribution.png)

### theme frequiency 
![theme frequency](outputs/visuals/theme_frequency.png)


---

## Key Insights

* **Drivers**: Fast navigation, simple interface, intuitive UX.
* **Pain Points**: Login/OTP failures, crashes, failed updates.
* **Top Negative Sentiment Themes**: Update Problems, Login Issues, App Bugs.

---

## Output Files

| File                         | Description                   |
| ---------------------------- | ----------------------------- |
| `reviews_with_sentiment.csv` | Reviews + Sentiment scores    |
| `bank_themes_bertopic.csv`   | Theme summary per bank        |
| `reviews_with_themes.csv`    | Merged sentiment + theme info |
| `*.png`                      | Visual insight plots          |

---

## Authors & Credits

Developed by **Nurye Nigus** 
Electrical and AI engineer.

---

## Contact

Have suggestions or feedback?
Open an issue or reach out via [LinkedIn](https://www.linkedin.com/in/nryngs).

---

