import streamlit as st
import pandas as pd
import plotly.express as px
from forecast_utils import train_forecaster, predict_future_usage

st.title("🔋 Smart Energy Usage Forecaster")
st.write("Upload your energy usage CSV file to see usage trends and future forecasts.")

uploaded_file = st.file_uploader("📤 Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data Sample")
    st.dataframe(df.head())

    if 'timestamp' not in df.columns or 'energy_kWh' not in df.columns:
        st.error("CSV must contain 'timestamp' and 'energy_kWh' columns.")
    else:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        st.write("### 📈 Energy Usage Over Time")
        fig = px.line(df, x='timestamp', y='energy_kWh', title='Historical Usage')
        st.plotly_chart(fig)

        model = train_forecaster(df)
        future_df = predict_future_usage(model, periods=48)

        st.write("### 🔮 Forecast: Next 48 Hours")
        fig2 = px.line(future_df, x='timestamp', y='predicted_energy_kWh', title='Forecasted Usage')
        st.plotly_chart(fig2)

        st.success("Done! Scroll above to explore data and forecast.")
