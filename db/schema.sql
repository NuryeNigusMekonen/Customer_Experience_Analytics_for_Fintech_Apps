CREATE TABLE bank_reviews (
    review            CLOB,
    rating            NUMBER(2),
    review_date       DATE,
    bank              VARCHAR2(100),
    source            VARCHAR2(100),
    sentiment_label   VARCHAR2(20),
    sentiment_score   BINARY_FLOAT
)
