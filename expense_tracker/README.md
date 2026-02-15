# 💰 Smart Expense Tracker

A clean, production-ready expense tracking application built with Python and Streamlit.

## Features
-   **Add Utilities**: Easily add expenses with date, category, and notes.
-   **Dashboard**: View total expenses, monthly trends, and recent transactions.
-   **Budget Management**: Set a monthly budget and get warnings if you exceed it.
-   **Visualizations**: Interactive charts for category distribution, monthly trends, and daily spending.
-   **Smart Prediction**: Basic linear regression model to predict future spending based on history.
-   **Data Management**: Download your expense data (filtered) as CSV.

## Tech Stack
-   **Python 3.x**
-   **Streamlit** (Frontend)
-   **Pandas** (Data Manipulation)
-   **Matplotlib** (Visualization)

## Installation

1.  Clone the repository or navigate to the project folder.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your default browser (usually at `http://localhost:8501`).

## Project Structure
```
expense_tracker/
│── app.py             # Main application
│── data_manager.py    # Data handling logic
│── visuals.py         # Visualization functions
│── data.csv           # persistent storage (auto-generated)
│── requirements.txt   # Dependencies
│── README.md          # This file
```

## Future Improvements
-   Database integration (SQLite/PostgreSQL) instead of CSV.
-   User Authentication.
-   More advanced authentication and multi-user support.
-   AI-powered expense categorization.
