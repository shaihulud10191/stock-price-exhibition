import yfinance as yf
import pandas as pd 
import json

seb = yf.Tickers('AAPL') #Instantiate a Ticker object from yf, enables use of methods that facilitate working with stock data
src = ('C:/Users/Kaustubh/Downloads/apple.json')
with open (src) as file:
    info = json.load(file) #info var now holds information about apple's stock

#Now, taking a look at its share price over time
hist_price = seb.history(period = 'max') #a df is generated period is arg for time period, set to max for all changes since ipo
hist_price.reset_index(inplace = True) #inplace ensures that the actual df's index is reset too
hist_price.head() #AAPL was listed in 1980, so head() will start around that time

print(hist_price.plot(x = 'Date', y = 'Open'))
#Taking a look at dividends. At first, I thought I could use the info json, but it doesn't have any long-term dividend info
seb.dividend
