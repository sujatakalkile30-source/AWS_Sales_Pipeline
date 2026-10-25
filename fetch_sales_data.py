import psycopg2
import pandas as pd

# RDS Connection Details
HOST_ENDPOINT = "sujata-sales-db.cxckcges0tns.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "SujataCloud2026"
PORT = "5432"

try:
    print("Connecting to AWS RDS to fetch sales data...")
    connection = psycopg2.connect(
        host=HOST_ENDPOINT,
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        port=PORT
    )
    
    # Query data directly into a pandas DataFrame
    query = "SELECT * FROM sales_data;"
    df = pd.read_sql(query, connection)
    
    print("\n--- AWS RDS Sales Data Table ---")
    print(df.to_string(index=False))
    print("---------------------------------")
    print("\nSUCCESS: Sales data retrieved successfully from Cloud Database!")

    connection.close()

except Exception as error:
    print(f"Error while fetching data: {error}")