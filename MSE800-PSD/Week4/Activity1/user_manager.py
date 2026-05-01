from database import create_connection
from datetime import datetime

class BankingManager:
    # ... (previous add_customer, create_account, and view_customers methods)[cite: 7]

    def add_currency(self, name, symbol, country):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO CURRENCY (currencyName, symbol, country, lastUpdated) 
                VALUES (?, ?, ?, ?)""", (name, symbol, country, datetime.now()))
            conn.commit()
            print(f"Currency {name} added.")
        finally:
            conn.close()

    def set_exchange_rate(self, curr_id, rate):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO EXCHANGE_RATE (rate, effectiveDate, curr_id) 
                VALUES (?, ?, ?)""", (rate, datetime.now(), curr_id))
            conn.commit()
            print(f"Exchange rate updated for Currency ID {curr_id}.")
        finally:
            conn.close()

    def record_transaction(self, account_id, amount, curr_id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            # 1. Record the transaction log
            cursor.execute("""
                INSERT INTO TRANSACTION_LOG (amount, account_id, curr_id) 
                VALUES (?, ?, ?)""", (amount, account_id, curr_id))
            
            # 2. Update the actual account balance
            cursor.execute("""
                UPDATE ACCOUNT SET balance = balance + ? 
                WHERE account_id = ?""", (amount, account_id))
            
            conn.commit()
            print(f"Transaction of {amount} recorded for Account {account_id}.")
        except Exception as e:
            print(f"Transaction failed: {e}")
        finally:
            conn.close()

    def view_transactions(self, account_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.tx_id, t.amount, t.timestamp, c.symbol 
            FROM TRANSACTION_LOG t 
            JOIN CURRENCY c ON t.curr_id = c.curr_id 
            WHERE t.account_id = ?""", (account_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    def view_customers(self):
        """Fetches and returns all customer records from the database."""
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMER")
        rows = cursor.fetchall()
        conn.close()
        return rows