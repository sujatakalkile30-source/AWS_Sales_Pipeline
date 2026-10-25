import psycopg2

# RDS Connection Details
HOST_ENDPOINT = "sujata-sales-db.cxckcges0tns.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
USER = "postgres"
PASSWORD = "SujataCloud2026"
PORT = "5432"

try:
    print("Connecting to AWS RDS to insert data...")
    connection = psycopg2.connect(
        host=HOST_ENDPOINT,
        database=DB_NAME,
        user=USER,
        password=PASSWORD,
        port=PORT
    )
    cursor = connection.cursor()

    # Sample Sales Data to insert
    sales_records = [
        ("Laptop", "Electronics", 2, 55000.00, "2026-10-20"),
        ("Mouse", "Electronics", 5, 500.00, "2026-10-21"),
        ("Keyboard", "Electronics", 3, 1200.00, "2026-10-22"),
        ("Desk Chair", "Furniture", 1, 7500.00, "2026-10-23"),
        ("Monitor", "Electronics", 2, 14000.00, "2026-10-24")
    ]

    insert_query = """
    INSERT INTO sales_data (product_name, category, quantity, price, sale_date)
    VALUES (%s, %s, %s, %s, %s);
    """

    cursor.executemany(insert_query, sales_records)
    connection.commit()
    print("SUCCESS: 5 Sales records inserted successfully into AWS RDS!")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error while inserting data: {error}")