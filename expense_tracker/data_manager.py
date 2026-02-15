import pandas as pd
import os
from datetime import datetime

DATA_FILE = "data.csv"

def load_data():
    """Lengths data from CSV or creates an empty DataFrame if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            # Ensure proper types
            df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])

def save_expense(date, category, amount, notes):
    """Saves a new expense to the CSV file."""
    new_data = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Amount": float(amount),
        "Notes": notes
    }])
    
    if os.path.exists(DATA_FILE):
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        new_data.to_csv(DATA_FILE, mode='w', header=True, index=False)

def calculate_metrics(df):
    """Calculates total expenses and monthly total."""
    if df.empty:
      return 0.0, 0.0
    
    total_expenses = df['Amount'].sum()
    
    # Current month total
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    monthly_mask = (df['Date'].dt.month == current_month) & (df['Date'].dt.year == current_year)
    monthly_expenses = df.loc[monthly_mask, 'Amount'].sum()
    
    return total_expenses, monthly_expenses

def get_monthly_spending_trend(df):
    """Groups data by month for bar chart."""
    if df.empty:
        return pd.Series()
    
    # Create a copy to avoid SettingWithCopyWarning on the original df
    df_copy = df.copy()
    df_copy['Month'] = df_copy['Date'].dt.to_period('M')
    return df_copy.groupby('Month')['Amount'].sum()

def get_category_distribution(df):
    """Groups data by category for pie chart."""
    if df.empty:
        return pd.Series()

def predict_spending(df):
    """Predicts next month's total spending using simple linear regression."""
    if df.empty or len(df) < 2:
        return 0.0

    # Aggregate by day
    daily_spending = df.groupby('Date')['Amount'].sum().reset_index()
    daily_spending['DayOrdinal'] = daily_spending['Date'].map(datetime.toordinal)

    if len(daily_spending) < 2:
        return 0.0

    # Simple Linear Regression
    X = daily_spending['DayOrdinal'].values
    y = daily_spending['Amount'].values

    n = len(X)
    numerator = n * sum(X * y) - sum(X) * sum(y)
    denominator = n * sum(X**2) - sum(X)**2

    if denominator == 0:
        return 0.0
    
    slope = numerator / denominator
    intercept = (sum(y) - slope * sum(X)) / n

    # Predict for next 30 days
    last_date = daily_spending['Date'].max()
    future_dates = [last_date.toordinal() + i for i in range(1, 31)]
    predicted_total = sum(slope * date + intercept for date in future_dates)
    
    return max(0, predicted_total)

