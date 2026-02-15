# 💰 Smart Expense Tracker

A clean and interactive Expense Tracking Web App built using **Python, Streamlit, and Pandas**.  

This application helps users record daily expenses, visualize spending patterns, monitor budgets, and gain insights into financial habits.

---

## 🚀 Live Demo

🔗 Demo Link: Not Deployed till Now 

Run locally using:

```bash
streamlit run app.py
```

---

## 📌 Features

### ➕ Add Expenses
- Amount (required)
- Category (Food, Travel, Rent, Shopping, Utilities, Other)
- Date picker
- Optional notes
- Automatic data storage in CSV

### 📊 Dashboard Overview
- Total spending
- Monthly total
- Highest spending category
- Recent transactions (last 5 entries)

### 📈 Data Visualization
- Category-wise Pie Chart
- Monthly Spending Bar Chart
- Spending Trend Line Graph
- Clean Matplotlib visualizations

### 🎯 Budget Tracking
- Set monthly budget
- Budget usage percentage
- A warning alert when the budget exceeds

### 📥 Extra Features (Optional)
- Download expense data as CSV
- Basic spending prediction
- Dark mode toggle (if implemented)

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|------------|
| Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Storage | CSV File |

---

## 📂 Project Structure

```
expense_tracker/
│── app.py
│── data.csv (auto-generated)
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 📊 Example Insights

- Total Spending: ₹12,450
- Highest Category: Food
- Budget Used: 78%
- Monthly Trend: Increasing

---

## 📈 How It Works

1. User inputs expense details.
2. Data is stored in `data.csv`.
3. Pandas processes data for aggregation.
4. Matplotlib generates charts.
5. Budget calculations compare total vs user-defined limit.

---

## 🧪 Error Handling

- Automatically creates `data.csv` if not found.
- Validates the amount input.
- Prevents invalid data entries.

---

## 🚀 Future Improvements

- SQLite database integration
- User authentication
- Multi-user support
- Cloud deployment
- Advanced forecasting model
- Export monthly PDF report

---


## 💼 Why This Project Is Portfolio-Ready

This project demonstrates:

- Data manipulation using Pandas  
- Interactive web app development  
- Data visualization  
- Budget logic implementation  
- Clean project structuring  
- Deployable Streamlit app  

---

## 📜 License

MIT License

---

## 👤 Author

Your Name  : Pawan Nikam
Final Year Engineering Student  
Interested in Data Science & Software Development, IOT  
