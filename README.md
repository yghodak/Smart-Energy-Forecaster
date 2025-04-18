# 🔋 Smart Energy Usage Forecaster

A Streamlit-based machine learning web app that predicts future energy consumption using historical data and a Random Forest regression model.

---

## 🚀 Features

- 📤 Upload your own energy usage CSV file
- 📈 Visualize historical energy consumption trends
- 🔮 Forecast future usage (next 48 hours by default)
- 🌐 Interactive UI built with Streamlit and Plotly

---

## 📁 Project Structure
```bash
Smart Energy Usage Forecaster/ 
│ 
├── app.py               # Main Streamlit application 
├── forecast_utils.py    # ML model logic and feature engineering 
├── .gitignore 
├── README.md 
└── requirements.txt     # Python dependencies
```
---


---

## 🧪 Sample Input CSV

Your uploaded CSV file must contain these columns:

| timestamp           | energy_kWh |
|---------------------|------------|
| 2025-01-01 00:00:00 | 1.23       |
| 2025-01-01 01:00:00 | 1.01       |
| ...                 | ...        |

- `timestamp`: Must be in a datetime format
- `energy_kWh`: The energy usage for that hour

---

## 📦 Installation

1. Clone the repo

```bash
git clone https://github.com/yghodak/Smart-Energy-Forecaster.git
cd Smart-Energy-Forecaster
```
2. Create and activate a virtual environment (optional)
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows use .venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

---
## ▶️ Run the App
```bash
streamlit run app.py
```
---
## 📊 Model Details

- `Algorithm`: Random Forest Regressor
- `Features Used`: Hour, Day, Weekday, Month extracted from timestamp
- `Target`: energy_kWh
- `Forecast Output`: Predicted usage for the next 24 to 48 hours

---

## 🛠️ Built With
```bash
Python, Pandas, Scikit-learn, Streamlit, Plotly
```

##  Author
### Yash Ghodake 🧑‍💻



