# Banking System

A command-line banking application built in Python with SQLite, supporting user registration, authentication, and core banking operations.


## Project Structure

```
banking/
├── main.py                  # Entry point
├── db/
│   ├── __init__.py
│   └── database.py          # DB initialization & connection
├── services/
│   ├── __init__.py
│   ├── bank_service.py      # Deposit, withdraw, balance operations
│   └── user_service.py      # Registration & authentication
└── utils/
    ├── __init__.py
    └── account_utils.py     # Account number generator
```



## Requirements

- Python 3.7+
- SQLite3 (built into Python standard library — no installation needed)



## Installation

**1. Clone or download the project:**
```bash
git clone <your-repo-url>
cd banking
```

**2. Run the application:**
```bash
python main.py
```

> The database file `banking_system.db` will be **auto-generated** on first run.



## Database Schema

The app uses a single SQLite table:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Auto-incremented primary key |
| `username` | TEXT | Unique login username |
| `password` | TEXT | User password |
| `name` | TEXT | Full name |
| `dob` | TEXT | Date of birth (DD/MM/YYYY) |
| `account_number` | TEXT | Unique 14-digit account number |
| `account_type` | TEXT | `Personal` or `Business` |
| `balance` | REAL | Account balance (default: 0) |
