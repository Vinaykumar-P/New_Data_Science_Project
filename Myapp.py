import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         
        ## Simple Stock Price app
        Shown are the stock price
     
        """)

tS='HDFCBANK.NS'
tD= yf.Ticker(tS)
#tDF=tD.history(start='2010-5-31', end='2020-5-31')
tDF = tD.history(start='2024-05-31', end='2025-08-29')
st.line_chart(tDF.Close)
st.line_chart(tDF.Volume)