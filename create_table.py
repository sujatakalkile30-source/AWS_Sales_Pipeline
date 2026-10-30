import psycopg2

# RDS Database Details
HOST_ENDPOINT = "your-rds-endpoint"
DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "Sujata"
PORT = "5432"

try:
    print("Connecting to RDS to recreate the table...")
    connection = psycopg2.connect(
        host=HOST_ENDPOINT,
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        port=PORT
    )
    cursor = connection.cursor()

    # Drop old table and create a fresh matching table
    cursor.execute("DROP TABLE IF EXISTS sales_data;")
    cursor.execute("""
        CREATE TABLE sales_data (
            id SERIAL PRIMARY KEY,
            product VARCHAR(100),
            category VARCHAR(100),
            quantity INT,
            price NUMERIC,
            sale_date DATE
        );
    """)
    
    connection.commit()
    print("SUCCESS: `sales_data` table recreated successfully with correct columns!")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error: {error}")
