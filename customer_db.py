import sqlite3

conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

# Drop the old table (⚠️ this deletes existing data)
cursor.execute('DROP TABLE IF EXISTS customers')

# Recreate with full schema
cursor.execute('''
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        birthday TEXT,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        preferred_contact TEXT
    )
''')

for column in ["street_address", "city", "state_province", "zip_postal"]:
    try:
        cursor.execute(f"ALTER TABLE customers ADD COLUMN {column} TEXT")
    except sqlite3.OperationalError:
        pass  # Already exists

conn.commit()
conn.close()

print("Table recreated with full schema.")