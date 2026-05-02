# 💱 Money Exchange System – ER Diagram

## 📌 Project Overview

This project presents an **Entity-Relationship (ER) Diagram** for a **Finance Money Exchange Software Application**. The system models how customers perform transactions involving different currencies, along with exchange rate tracking[cite: 1].

---

## 🧩 Entities and Attributes

### 1. CUSTOMER

* customer_id (PK)
* first_name
* last_name
* email
* phone

---

### 2. ACCOUNT

* account_id (PK)
* customer_id (FK)
* balance
* acc_type

---

### 3. TRANSACTION_LOG

* tx_id (PK)
* account_id (FK)
* curr_id (FK)
* amount
* timestamp

---

### 4. CURRENCY

* curr_id (PK)
* CurrencyName
* Symbol
* Country
* LastUpdated

---

### 5. EXCHANGE RATE

* rate_id (PK)
* curr_id (FK)
* Rate
* EffectiveDate

---
### 6. ACC_CUST

* account_id (FK)
* customer_id (FK)




## 🔗 Relationships

| Relationship | Type | Description |
| :--- | :--- | :--- |
| CUSTOMER ↔ ACCOUNT | M:N | Linked via the ACC_CUST associative entity. |
| ACCOUNT ↔ TRANSACTION | 1:N | Tracks history across different accounts. |
| TRANSACTION ↔ CURRENCY | 1:1 | Each transaction record is associated with one currency. |
| EXCHANGE RATE ↔ CURRENCY | N:1 | Multiple rates can be defined for a single currency. |

---