import yfinance as yf
import streamlit as st

import pandas as pd

st.write("""
         
        # Simple Stock Tracking app
        ### Congratulations Vinay you did it!
     
        """)
# Get current date and time


tS='HDFCBANK.NS'
tD= yf.Ticker(tS)
#tDF=tD.history(start='2010-5-31', end='2020-5-31')
tDF = tD.history(start='2022-04-01')
st.line_chart(tDF.Close)
st.line_chart(tDF.Volume)
