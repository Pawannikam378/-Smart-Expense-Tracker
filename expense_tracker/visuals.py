import matplotlib.pyplot as plt
import pandas as pd

def plot_category_distribution(category_data):
    """Generates a pie chart for category distribution."""
    fig, ax = plt.subplots(figsize=(6, 6))
    if category_data.empty:
        ax.text(0.5, 0.5, "No data available", ha='center', va='center')
        ax.axis('off')
        return fig
    
    ax.pie(category_data, labels=category_data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Expense Distribution by Category")
    return fig

def plot_monthly_trend(monthly_data):
    """Generates a bar chart for monthly spending."""
    fig, ax = plt.subplots(figsize=(8, 4))
    if monthly_data.empty:
        ax.text(0.5, 0.5, "No data available", ha='center', va='center')
        ax.axis('off')
        return fig
    
    monthly_data.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Monthly Spending Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    plt.xticks(rotation=45)
    return fig

def plot_spending_over_time(df):
    """Generates a line chart for spending over time."""
    fig, ax = plt.subplots(figsize=(8, 4))
    if df.empty:
        ax.text(0.5, 0.5, "No data available", ha='center', va='center')
        ax.axis('off')
        return fig
        
    daily_spending = df.groupby('Date')['Amount'].sum()
    daily_spending.plot(kind='line', ax=ax, marker='o', linestyle='-', color='green')
    ax.set_title("Daily Spending Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Amount")
    plt.grid(True)
    return fig
