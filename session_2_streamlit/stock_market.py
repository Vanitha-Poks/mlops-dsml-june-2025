import streamlit as st
import pandas as pd
import numpy as np

#pip install yfinance

import yfinance as yf


st.title('Stock Market Data Analysis')

# Header
#st.header("This is a header")
 
## Subheader
#st.subheader("This is a subheader")

#st.write("# Welcome to Streamlit! 👋")

#ticker_symbol = 'AAPL'  # Default ticker symbol
ticker_symbol = st.text_input("Please enter Ticker Symbol", 'AAPL')

ticker_data = yf.Ticker(ticker_symbol)



import datetime

start_date = st.date_input("Please enter Starting Date",
              datetime.date(2019,1,1))

end_date = st.date_input("Please enter End Date",
              datetime.date(2022,12,31))


ticker_df = ticker_data.history(period='1d', start='2019-1-1', end='2022-10-1')

st.dataframe(ticker_df)


st.write("## Closing Price of " + ticker_symbol)
st.line_chart(ticker_df.Close)

st.write("## Volume of " + ticker_symbol)
st.line_chart(ticker_df.Volume)

column1, col2 = st.columns(2)

with column1:
	st.write("## Opening Price of " + ticker_symbol)
	st.line_chart(ticker_df.Open)
	#st.write("## Low Price of " + ticker_symbol)
	#st.line_chart(ticker_df.Low)

#with col2:
#	st.write("## High Price of " + ticker_symbol)
#	st.line_chart(ticker_df.High)

col2.container().write("## High Price of " + ticker_symbol)
col2.container().line_chart(ticker_df.High)



#if st.checkbox("Show/Hide"):
   
#  # display the text if the checkbox returns True value
#  st.text("Showing the widget")

#status = st.radio("Select Gender: ", ('Male', 'Female'))
#st.write("You selected:", status)


#if (status == 'Male'):
#    st.success("Male")
#else:
#    st.success("Female")
    

## Create a button, that when clicked, shows a text
#if(st.button("Click me")):
#    st.text("button click")
    

#def sqr(num):
    
#    return num*num


#num = st.number_input('Insert a number')

#if(st.button("Calculate Square")):
#    result = sqr(num)
#    st.text("Square of " + str(num) + " is " + str(result))