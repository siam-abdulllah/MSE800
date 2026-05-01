import sqlite3

def create_connection():
    return sqlite3.connect("banking_system.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CUSTOMER (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACCOUNT (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance REAL DEFAULT 0.0,
            acc_name TEXT,
            acc_type TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACC_CUST (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            customer_id INTEGER,
            FOREIGN KEY (account_id) REFERENCES ACCOUNT (account_id),
            FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CURRENCY (
            curr_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currencyName TEXT NOT NULL,
            symbol TEXT,
            country TEXT,
            lastUpdated DATETIME
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TRANSACTION_LOG (
            tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            curr_id INTEGER,
            account_id INTEGER,
            FOREIGN KEY (account_id) REFERENCES ACCOUNT (account_id),
            FOREIGN KEY (curr_id) REFERENCES CURRENCY (curr_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EXCHANGE_RATE (
            rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            rate REAL,
            effectiveDate DATETIME,
            curr_id INTEGER,
            FOREIGN KEY (curr_id) REFERENCES CURRENCY (curr_id)
        )
    ''')

    conn.commit()
    conn.close()