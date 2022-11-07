import yfinance as yf
import csv
from Stock import Stock
from get_all_tickers import get_tickers as gt
from get_all_tickers.get_tickers import Region


#data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
'''
msft = yf.Ticker("MSFT")
print(msft.info)
print(msft.dividends)
print(msft.splits)
print(msft.major_holders)
'''
class GetData:

	def __init__(self):

		#tickers = self.getPortfolio() #define tickers
		tickers = gt.get_biggest_n_tickers(1)

		self.dataTickers = []
		#tickers = ['msft', 'aapl', 'goog']
		for x in tickers:
			y = yf.Ticker(x)
			temp = y.info
			s = Stock(temp)
			self.dataTickers += [s]

	def getPortfolio(self):
		csvfile = "portfolio.csv"
		stockList = []
		with open(csvfile, 'r') as f:
				data = csv.reader(f)
				for symbol, companyName, costBasis, shareCount in data:
					stockList += [str(symbol)]

		return stockList


	def retData(self):
		return self.dataTickers