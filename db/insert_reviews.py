import oracledb
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(".."))
from db.db_config import ORACLE_CONFIG

schema_file_path = os.path.join(os.path.dirname(__file__), "schema.sql")

def create_table_if_not_exists(cursor, schema_file_path):
    cursor.execute("""
        SELECT COUNT(*) FROM user_tables WHERE table_name = 'BANK_REVIEWS'
    """)
    if cursor.fetchone()[0] == 0:
        print("Table 'BANK_REVIEWS' does not exist. Creating now...")
        with open(schema_file_path, 'r') as f:
            sql = f.read()
        cursor.execute(sql)
        print("Table created successfully.")
    else:
        print("Table already exists.")

def insert_reviews_from_csv(csv_path, schema_file_path):
    df = pd.read_csv(csv_path)
    df.fillna('', inplace=True)

    conn = oracledb.connect(
        user=ORACLE_CONFIG["user"],
        password=ORACLE_CONFIG["password"],
        dsn=ORACLE_CONFIG["dsn"]
    )
    cursor = conn.cursor()

    create_table_if_not_exists(cursor, schema_file_path)

    insert_sql = """
        INSERT INTO bank_reviews (
            review, rating, review_date, bank, source,
            sentiment_label, sentiment_score
        )
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_sql, (
            row['review'],
            int(row['rating']),
            row['date'],
            row['bank'],
            row['source'],
            row.get('sentiment_label', ''),
            float(row.get('sentiment_score', 0.0))
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted {len(df)} records into Oracle DB.")
