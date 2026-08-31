# Personal Finance Manager 💰

A simple Python-based command-line application for managing income, expenses, transactions, and remaining balance.

## Features

* Add income
* Add expenses
* Categorize expenses
* View expense transactions
* Calculate total income
* Calculate total expenses
* Calculate remaining balance
* 80% spending warning
* Automatically record transaction date and time
* Store financial data using `.txt` files
* Basic error handling for invalid input

## Technologies Used

* Python
* File Handling
* Functions
* Exception Handling
* `datetime` Module

## How It Works

The application provides a menu-driven interface:

```text
1. Add Income
2. Add Expense
3. View Transactions
4. Show Balance
5. Show Summary
6. Exit
```

Income and expense information is stored locally in text files, allowing the application to retrieve the data when it is run again.

Expense transactions are stored with their:

* Amount
* Category
* Date
* Time

## Project Structure

```text
Personal-Finance-Manager/
│
├── main.py
├── income.txt
├── expense.txt
└── README.md
```

## Example Transaction

```text
500 : Food : 2026-08-31 : 14:30:00
```

## Future Improvements

* Better input validation
* Monthly and yearly expense tracking
* Category-wise expense analysis
* Improved transaction display
* Separate modules for better code organization
* Graphical user interface
* Database-based data storage

## About This Project

This project was built as a Python learning project to practice programming concepts such as functions, file handling, exception handling, modules, and working with dates and times.

It will be improved over time as new Python and software development concepts are learned.
