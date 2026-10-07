# EquiMatch 📈

### Multi-User Equity Order Book & Order Matching System

EquiMatch is a Python-based equity order book and order matching system designed to simulate how buy and sell orders can be placed, stored, prioritized, and matched in a trading environment.

The project started as a Python order-matching system and is being extended into a **multi-user trading application with MySQL database integration**.

---

## 🚀 Project Overview

EquiMatch allows users to:

* Create and manage user accounts
* Log in using email and password
* Place BUY and SELL orders
* Specify stock symbols, quantities, and prices
* Maintain an order book
* Match compatible BUY and SELL orders
* Support partial order execution
* Maintain order statuses
* Store orders and trades in MySQL
* View user-specific order history
* Maintain trade history
* Support multiple users trading through a shared order book

The main objective of the project is to understand the **logic behind an equity order book and order matching system** while gradually building it into a multi-user application.

---

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **MySQL Connector/Python**
* **Object-Oriented Programming (OOP)**
* **SQL**
* **Django / REST API** — planned
* **Git & GitHub**

---

## 🏗️ Project Architecture

The project is being developed in multiple stages:

```text
Stage 1 → Python Order Book Logic
Stage 2 → MySQL Database Integration
Stage 3 → Multi-User Trading System
Stage 4 → Django / REST API
```

### Current Project Structure

```text
EquiMatch/
│
├── main.py
│
├── models/
│   └── order.py
│
├── orderbook/
│   └── order_book.py
│
└── database/
    └── connection.py
```

---

## 📌 Core Features

### 👤 User Authentication

Users can log in using:

* Email
* Password

The system identifies the logged-in user using their `user_id`.

---

### 📋 Order Management

Users can place:

* BUY orders
* SELL orders

Each order contains information such as:

```text
Order ID
User ID
Stock Symbol
Side
Quantity
Price
Timestamp
Status
```

---

### 📖 Order Book

The order book maintains separate:

```text
BUY ORDERS
SELL ORDERS
```

Orders are prioritized using **price-time priority**.

For BUY orders:

```text
Higher price → Higher priority
Earlier timestamp → Higher priority
```

For SELL orders:

```text
Lower price → Higher priority
Earlier timestamp → Higher priority
```

---

### 🔄 Order Matching

A BUY order can match a SELL order when:

```text
BUY price >= SELL price
```

The system calculates the executable quantity based on the available quantities of both orders.

Example:

```text
BUY  → 50 RELIANCE @ ₹1500
SELL → 20 RELIANCE @ ₹1400
```

Result:

```text
Trade Quantity → 20
Remaining BUY → 30
SELL → Fully Filled
```

---

### 📊 Partial Execution

The system supports partially filled orders.

Example:

```text
BUY → 100 @ ₹1500
SELL → 40 @ ₹1400
```

After matching:

```text
BUY remaining → 60
SELL remaining → 0
```

The BUY order becomes:

```text
PARTIALLY_FILLED
```

---

## 📌 Order Status

EquiMatch currently uses three order statuses:

| Status             | Description                         |
| ------------------ | ----------------------------------- |
| `PENDING`          | Order is waiting to be matched      |
| `PARTIALLY_FILLED` | Part of the order has been executed |
| `FILLED`           | Entire order has been executed      |

Only active orders (`PENDING` and `PARTIALLY_FILLED`) are loaded into the active order book.

---

## 🗄️ Database

EquiMatch uses **MySQL** for persistent data storage.

### Database

```text
EquiMatch_db
```

### Main Tables

```text
users
orders
trades
```

### Users

Stores user account information.

```text
user_id
user_name
email
password
```

### Orders

Stores all BUY and SELL orders.

```text
order_id
user_id
symbol
side
quantity
price
timestamp
status
```

### Trades

Stores completed executions.

```text
trade_id
buy_order_id
sell_order_id
quantity
price
```

---

## 🔗 Database Relationships

The main relationships are:

```text
users
   │
   │ user_id
   ▼
orders
   │
   ├──────────────► buy_order_id
   │
   └──────────────► sell_order_id
                       │
                       ▼
                     trades
```

This allows the system to determine which users participated in a particular trade.

---

## 👥 Multi-User Trading

EquiMatch is designed around a shared order book.

For example:

```text
User 1
BUY RELIANCE
50 shares @ ₹1500
```

and:

```text
User 2
SELL RELIANCE
20 shares @ ₹1400
```

The orders can be matched because:

```text
1500 >= 1400
```

The trade is stored in the `trades` table and both users can later identify their participation through their corresponding order IDs.

---

## 📜 Order History

Users can view orders belonging to their own account.

The system uses the logged-in user's `user_id` to retrieve their orders.

This allows each user to see their own:

* Order ID
* Stock symbol
* BUY/SELL side
* Quantity
* Price
* Status

---

## 📈 Trade History

Trade history is built using the relationship between:

```text
users → orders → trades
```

A user's order can appear in a trade as either:

```text
buy_order_id
```

or:

```text
sell_order_id
```

This allows the system to identify trades in which the logged-in user participated as either a buyer or seller.

---

## 🧪 Example

### User 1

```text
BUY RELIANCE
Quantity: 50
Price: ₹1500
```

### User 2

```text
SELL RELIANCE
Quantity: 20
Price: ₹1400
```

### Matching Result

```text
Trade
-------------------------
Quantity: 20
Price: ₹1500

User 1
Remaining: 30
Status: PARTIALLY_FILLED

User 2
Remaining: 0
Status: FILLED
```

---

## 🎯 Project Goals

The main goals of EquiMatch are:

* Understand order book architecture
* Practice Python OOP
* Implement price-time priority
* Understand order matching
* Work with relational databases
* Practice SQL JOINs and foreign keys
* Build a multi-user system
* Understand how trading systems maintain order and trade records
* Gradually convert the application into a web-based system

---

# 🔮 Future Enhancements

The project will be expanded gradually.

### 🌐 Django Web Application

Convert the current command-line application into a Django-based web application.

Planned features:

* User registration
* Login/logout
* User dashboard
* Order placement interface
* Order book interface
* Order history
* Trade history

---

### 🔌 REST API

Build APIs for:

* User authentication
* Order creation
* Order cancellation
* Order book
* Trade history
* Order history

---

### ⚡ Real-Time Order Book

Add real-time updates so users can see changes to the order book without manually refreshing the page.

Possible technologies:

* WebSockets
* Django Channels

---

### ❌ Order Cancellation

Allow users to cancel active orders that have not been completely filled.

The system will need to handle:

```text
PENDING → CANCELLED
```

and potentially cancellation of the remaining quantity of a partially filled order.

---

### 📊 Trading Dashboard

Create a dashboard containing:

* Active orders
* Completed orders
* Trade history
* Order book
* User trading activity
* Stock information

---

### 📈 Market Data

Integrate external market-data APIs to display real-time or delayed stock prices.

---

### 💰 Portfolio Management

Add portfolio functionality to track:

* Holdings
* Available balance
* Buy transactions
* Sell transactions
* Average purchase price
* Portfolio value

---

### 🔐 Improved Security

Improve authentication and data security by adding:

* Password hashing
* Secure authentication
* Input validation
* Better database security
* Authorization checks

---

### 🧵 Concurrency & Multiple Requests

Improve the matching engine to safely handle multiple users placing orders at approximately the same time.

This will be important when moving from a simple Python application to a real web-based multi-user system.

---

### 🧪 Automated Testing

Add unit and integration tests for:

* Order creation
* Order validation
* Order matching
* Partial fills
* Multiple matches
* Price-time priority
* Database operations
* User authentication

---

## 📚 Learning Outcomes

Through this project, I am practicing and improving my understanding of:

* Python
* Object-Oriented Programming
* Data structures
* Algorithms
* SQL
* MySQL
* Database relationships
* Foreign keys
* JOIN operations
* Multi-user application design
* Order matching algorithms
* Backend development
* API development

---

## 🚧 Project Status

**Current Status: In Development 🚧**

Completed:

* [x] Python Order Book
* [x] BUY/SELL order handling
* [x] Price-time priority
* [x] Order matching
* [x] Partial execution
* [x] Order status management
* [x] MySQL integration
* [x] User authentication
* [x] User-specific order history
* [x] Multi-user order matching foundation
* [x] Trade storage

In Progress:

* [ ] User-specific trade history
* [ ] Complete multi-user workflow
* [ ] Order cancellation
* [ ] Django web application
* [ ] REST API
* [ ] Real-time order book

---

## 👨‍💻 Author

**Albin George**

BCA Graduate | Python & Django Full Stack Developer

Interested in:

* Python Development
* Django
* Backend Development
* Databases
* APIs
* AI & Machine Learning

---

## ⭐ Future Vision

EquiMatch is being developed incrementally from a Python-based order matching engine into a **multi-user web-based equity trading simulation platform**.

The focus is on understanding the underlying backend logic, database architecture, and order-matching process while continuously adding real-world features.
