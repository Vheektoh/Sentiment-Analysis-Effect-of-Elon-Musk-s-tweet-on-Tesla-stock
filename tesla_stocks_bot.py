#stocks bot to pull Elon Musk's Tesla's stock data

import yfinance as yf





#Get Tesla's stocks data of the date range we're working with (from 2022-07-25 to 2022-08-01 with an interval = '1m')
tesla_stocks = yf.download('TSLA', start = '2022-07-25', end = '2022-08-01', interval = '1m')


#Export Tesla's stocks as csv
tesla_stocks.to_csv('data/tesla_stocks.csv')