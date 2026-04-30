\# 💱 Money Exchange System – ER Diagram



\## 📌 Project Overview



This project presents an \*\*Entity-Relationship (ER) Diagram\*\* for a \*\*Finance Money Exchange Software Application\*\*.

The system models how customers perform transactions involving different currencies, along with exchange rate tracking.



\---



\## 🧩 Entities and Attributes



\### 1. CUSTOMER



\* \*\*customer\_id (PK)\*\*

\* first\_name

\* last\_name

\* email

\* phone



\---



\### 2. ACCOUNT



\* \*\*account\_id (PK)\*\*

\* customer\_id (FK)

\* balance

\* acc\_type

\* created\_at



\---



\### 3. TRANSACTION



\* \*\*tx\_id (PK)\*\*

\* account\_id (FK)

\* amount

\* timestamp

\* curr\_id (FK)



\---



\### 4. CURRENCY



\* \*\*curr\_id (PK)\*\*

\* CurrencyName

\* Symbol

\* Country

\* LastUpdated



\---



\### 5. EXCHANGE RATE



\* \*\*rate\_id (PK)\*\*

\* curr\_id (FK) \*(From Currency)\*

\* ToCurrency (FK)

\* Rate

\* EffectiveDate



\---



\## 🔗 Relationships



| Relationship                            | Type  | Description                                      |

| --------------------------------------- | ----- | ------------------------------------------------ |

| CUSTOMER → ACCOUNT                      | 1 : N | One customer can have multiple accounts          |

| ACCOUNT → TRANSACTION                   | 1 : N | One account can have many transactions           |

| TRANSACTION → CURRENCY                  | N : 1 | Each transaction uses one currency               |

| CURRENCY → EXCHANGE RATE                | 1 : N | One currency can have multiple exchange rates    |

| CURRENCY ↔ CURRENCY (via Exchange Rate) | M : N | Currency conversion between different currencies |



\---



