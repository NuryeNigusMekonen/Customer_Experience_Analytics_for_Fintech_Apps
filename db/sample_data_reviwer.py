import oracledb
import pandas as pd
from db.db_config import ORACLE_CONFIG
def print_sample_reviews(limit=10):
    conn = oracledb.connect(
        user=ORACLE_CONFIG["user"],
        password=ORACLE_CONFIG["password"],
        dsn=ORACLE_CONFIG["dsn"]
    )
    cursor = conn.cursor()
    
    query = f"SELECT * FROM app_reviews WHERE ROWNUM <= {limit}"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # Get column names
    
    # Print column names
    print(columns)
    
    # Print rows
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()

# Call the function to print 5 sample rows
print_sample_reviews()