import psycopg2

# AWS RDS Configuration Details
HOST_ENDPOINT = "your-rds-endpoint"
DB_NAME = "postgres"
USER_NAME = "postgres"
PASSWORD_DB = "Sujata"
PORT_NUM = "5432"

try:
    print("Connecting to AWS RDS PostgreSQL Cloud Database...")
    conn = psycopg2.connect(
        host=HOST_ENDPOINT,
        database=DB_NAME,
        user=USER_NAME,
        password=PASSWORD_DB,
        port=PORT_NUM
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print("\n" + "="*50)
    print("SUCCESS: Connected to AWS RDS PostgreSQL successfully!")
    print(f"Database Version: {db_version[0]}")
    print("="*50 + "\n")
    
    cursor.close()
    conn.close()

except Exception as e:
    print("\nConnection Failed! Error details:")
    print(e)
