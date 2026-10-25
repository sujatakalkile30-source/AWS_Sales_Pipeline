import boto3
import pandas as pd
import psycopg2
from io import StringIO

# --- 1. CONFIGURATION ---
# S3 Details
BUCKET_NAME = "sujata-sales-data-2026"  # Replace with your actual S3 bucket name
FILE_NAME = "sales_data.csv"                  # The CSV file stored in your S3 bucket

# AWS RDS PostgreSQL Database Details
HOST_ENDPOINT = "sujata-sales-db.cxckcges0tns.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "SujataCloud2026"
PORT = "5432"

try:
    print("1. Connecting to AWS S3 to fetch the sales CSV file...")
    s3_client = boto3.client('s3')
    
    # Fetch file content directly from S3 bucket into memory
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
    csv_content = response['Body'].read().decode('utf-8')
    
    # Read CSV content into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_content))
    print(f"SUCCESS: Read {len(df)} records from S3 bucket successfully!")
    print("\n--- Preview of S3 Data ---")
    print(df)

    print("\n2. Connecting to AWS RDS PostgreSQL Database...")
    connection = psycopg2.connect(
        host=HOST_ENDPOINT,
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        port=PORT
    )
    cursor = connection.cursor()

    print("\n3. Ingesting S3 data into RDS table (`sales_data`)...")
    # Iterate through each row of the DataFrame and insert into PostgreSQL database
    for index, row in df.iterrows():
        insert_query = """
            INSERT INTO sales_data (product, category, quantity, price, sale_date)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            row['Product'], 
            row['Category'], 
            int(row['Quantity']), 
            float(row['Price']), 
            row['Date']
        ))

    # Commit transactions to save changes in the database
    connection.commit()
    print("SUCCESS: All S3 sales data successfully loaded into AWS RDS PostgreSQL Database!")

    # Close connection resources
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error during S3 to RDS pipeline execution: {error}")