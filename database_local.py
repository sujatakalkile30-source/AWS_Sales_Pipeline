import sqlite3
import pandas as pd

# 1. Connect to local SQL database file (Creates it if it doesn't exist)
conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

# 2. Create SQL Table for transactions
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

conn.commit()
print("SUCCESS: SQL Table 'transactions' created successfully in sales_database.db!")
conn.close()