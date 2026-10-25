import pandas as pd
import sqlite3
import random
from datetime import datetime

print("1. Generating sales data...")
# Generate sample data
customers = ["Sujata", "Amit", "Priya", "Rahul", "Sneha"]
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Wireless Mouse", "price": 800},
    {"name": "Mechanical Keyboard", "price": 2500},
    {"name": "HD Monitor", "price": 12000},
    {"name": "Headphones", "price": 3000}
]

sales_data = []
for i in range(1, 6):
    prod = random.choice(products)
    qty = random.randint(1, 3)
    transaction = {
        "TransactionID": 1000 + i,
        "CustomerName": random.choice(customers),
        "ProductName": prod["name"],
        "UnitPrice": prod["price"],
        "Quantity": qty,
        "TotalAmount": prod["price"] * qty,
        "TransactionDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    sales_data.append(transaction)

df = pd.DataFrame(sales_data)
csv_file = "daily_sales_data.csv"
df.to_csv(csv_file, index=False)
print("-> CSV file 'daily_sales_data.csv' created successfully!")

print("\n2. Connecting to Local SQL Database and saving data...")
# Connect to local SQLite database (creates sales_database.db automatically)
conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    TransactionID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    ProductName TEXT,
    UnitPrice REAL,
    Quantity INTEGER,
    TotalAmount REAL,
    TransactionDate TEXT
)
''')

# Insert data into SQL table
df.to_sql('transactions', conn, if_exists='replace', index=False)
conn.commit()
print("-> Data inserted into SQL database successfully!")

# 3. Read back from SQL to verify
print("\n3. Fetching and printing data from SQL Database:")
df_from_sql = pd.read_sql_query("SELECT * FROM transactions", conn)
print(df_from_sql)

conn.close()
print("\nSUCCESS! Day 2 local database processing completed successfully!")