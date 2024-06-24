import yfinance as yf
import streamlit as st
import pandas as pd

st.write ("""
# Simple Stock Price App
          
Shown are the **closing** stock price and **volume** of Apple!
"""
)
# define tinker Simbol
tinkerSymbol = "AAPL"

#Get data on for this stock
tickerData = yf.Ticker(tinkerSymbol)

tickerDf = tickerData.history(period='1d', start='2000-5-31', end='2024-6-20')

# Open High    Low Close   Volume  Dividends   Stocks Splits

# Display chart for Price and Volume
st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)
