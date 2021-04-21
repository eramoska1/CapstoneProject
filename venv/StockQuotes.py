# Getting Stocks from Yahoo Finance
# Tutorial
# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e


import yfinance as yf
import numpy
import pandas

def get_price(ticker):
    # setting the ticker
    stock = yf.Ticker(f"{ticker}")

    # printing stock info
    print(stock.info)

    # getting historical data
    # last 5 days in 60 minute intervals
    # can also use start/end, yyyy-mm-dd string
    hist = stock.history(period="5d",interval="60m")
    hist.to_csv(f'{ticker} prices.csv')
get_price('GME')
