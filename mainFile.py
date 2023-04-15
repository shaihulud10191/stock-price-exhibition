import yfinance as yf
import pandas as pd 
import json
seb = yf.Ticker('AAPL') #Instantiate a Ticker object from yf, enables use of methods that facilitate working with stock data
src = ('C:/Users/Kaustubh/Downloads/apple.json')
with open (src) as file:
    info = json.load(file) #info var now holds information about apple's stock
#Now, taking a look at its share price over time
hist_price = seb.history(period = 'max') #period is arg for time period, set to max for all changes since ipo
print(hist_price.head()) #AAPL was listed in 1980, so head() will start around that time

