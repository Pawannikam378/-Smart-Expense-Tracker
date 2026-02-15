import streamlit as st
import pandas as pd
import data_manager as dm
import visuals as vis
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Smart Expense Tracker", page_icon="💰", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("💰 Smart Expense Tracker")

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Add Expense", "Set Budget"])

    # Load data
    df = dm.load_data()

    if page == "Dashboard":
        show_dashboard(df)
    elif page == "Add Expense":
        show_add_expense()
    elif page == "Set Budget":
        show_set_budget(df)

def show_dashboard(df):
    st.header("Dashboard")
    
    if df.empty:
        st.info("No expenses recorded yet. Go to 'Add Expense' to get started!")
        return

    # Filter by Date
    st.sidebar.subheader("Filter Data")
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
    
    start_date = st.sidebar.date_input("Start Date", min_date)
    end_date = st.sidebar.date_input("End Date", max_date)
    
    mask = (df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)
    filtered_df = df.loc[mask]

    # Calculate metrics on FULL data for total context, or filtered? 
    # Usually dashboard metrics follow the filter.
    total_expenses = filtered_df['Amount'].sum()
    
    # Monthly calculation usually implies "current month", which might be outside filter.
    # But let's show stats for the filtered period.
    
    # Budget Check (Always against current month real-time, independent of filter)
    # Re-calculate monthly expenses for budget specifically
    _, current_month_expenses = dm.calculate_metrics(df)
    
    budget = st.session_state.get('budget', 0.0)
    
    # Metrics Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Expenses (Selection)", f"${total_expenses:,.2f}")
    col2.metric("Current Month (Total)", f"${current_month_expenses:,.2f}")
    
    if budget > 0:
        remaining = budget - current_month_expenses
        percent_used = (current_month_expenses / budget) * 100
        col3.metric("Remaining Budget", f"${remaining:,.2f}", delta_color="normal" if remaining >= 0 else "inverse")
        if remaining < 0:
            st.error(f"⚠️ You have exceeded your monthly budget of ${budget:,.2f}!")
        else:
            st.progress(min(percent_used / 100, 1.0))
            st.caption(f"{percent_used:.1f}% of budget used")
    else:
        col3.metric("Budget", "Not Set")

    # Prediction (Bonus) - Based on all history
    prediction = dm.predict_spending(df)
    if prediction > 0:
         st.sidebar.info(f"🔮 Predicted Spending (Next 30 Days): ${prediction:,.2f}")

    # Charts Row 1
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Spending by Category")
        category_dist = dm.get_category_distribution(filtered_df)
        st.pyplot(vis.plot_category_distribution(category_dist))
        
    with col_chart2:
        st.subheader("Monthly Trend")
        # For trend, we might want to see the whole trend or just selection? 
        # Usually trend is better with more context, but let's stick to filter for consistency.
        monthly_trend = dm.get_monthly_spending_trend(filtered_df)
        st.pyplot(vis.plot_monthly_trend(monthly_trend))

    # Charts Row 2
    st.subheader("Daily Spending")
    vis_fig = vis.plot_spending_over_time(filtered_df)
    st.pyplot(vis_fig)

    # Recent Transactions
    st.subheader("Recent Transactions (Filtered)")
    st.dataframe(filtered_df.sort_values(by="Date", ascending=False).head(5), use_container_width=True)
    
    # Download Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='expense_data.csv',
        mime='text/csv',
    )

def show_add_expense():
    st.header("Add New Expense")
    
    with st.form("expense_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.now())
        category = st.selectbox("Category", ["Food", "Travel", "Rent", "Shopping", "Utilities", "Other"])
        amount = st.number_input("Amount", min_value=0.01, step=0.01, format="%.2f")
        notes = st.text_area("Notes (Optional)")
        
        submitted = st.form_submit_button("Save Expense")
        
        if submitted:
            if amount > 0:
                dm.save_expense(date, category, amount, notes)
                st.success("Expense saved successfully!")
            else:
                st.error("Amount must be greater than 0")

def show_set_budget():
    st.header("Set Monthly Budget")
    
    current_budget = st.session_state.get('budget', 0.0)
    new_budget = st.number_input("Enter Monthly Budget Limit ($)", min_value=0.0, value=current_budget, step=50.0)
    
    if st.button("Update Budget"):
        st.session_state['budget'] = new_budget
        st.success(f"Budget updated to ${new_budget:,.2f}")

if __name__ == "__main__":
    main()
