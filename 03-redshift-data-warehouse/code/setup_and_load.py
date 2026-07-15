import boto3
import psycopg2

CLUSTER_ENDPOINT = "your-cluster.redshift.amazonaws.com"
DB_NAME = "dev"
DB_USER = "awsuser"
DB_PASSWORD = "password"
IAM_ROLE = "arn:aws:iam::account:role/RedshiftS3ReadOnly"
S3_PATH = "s3://my-bucket/sales-data/"

conn = psycopg2.connect(
    host=CLUSTER_ENDPOINT,
    port=5439,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sale_date DATE,
    price DECIMAL(10, 2)
);
""")

cursor.execute(f"""
COPY sales
FROM '{S3_PATH}'
IAM_ROLE '{IAM_ROLE}'
CSV IGNOREHEADER 1;
""")
conn.commit()

cursor.execute("SELECT product_id, SUM(quantity * price) AS revenue FROM sales GROUP BY product_id ORDER BY revenue DESC LIMIT 10;")
for row in cursor.fetchall():
    print(row)

conn.close()
