from Stock import Stock
import csv

class Portfolio:
	def __init__(self):
 
		self.csvfile = "portfolio.csv"

		f = open(self.csvfile, 'a+')
		f.close()
		self.stockList = []

		with open(self.csvfile, 'r') as f:
			data = csv.reader(f)
			for symbol, companyName, costBasis, shareCount in data:
				x = Stock(symbol, companyName, costBasis, shareCount)
				self.stockList += [x]

	def getPortfolio(self):
		print("getPortfolio")
		for x in self.stockList:
			print(x.printInfo())

	def add(self, stock):
		print("addToPortfolio")
		self.stockList += [stock]
		fields=[stock.symbol, stock.companyName, stock.costBasis, stock.shareCount]
		with open(self.csvfile,'a', newline="") as f:
			print("writing")
			writer = csv.writer(f) 
			writer.writerow(fields)

	def remove(self, stock):
		with open(self.csvfile, "w", newline="") as f:
			writer = csv.writer(f)
			for x in self.stockList:
				if not x.symbol == stock:
					fields=[x.symbol, x.companyName, x.costBasis, x.shareCount]
					writer.writerow(fields)
				else:
					self.stockList.remove(x)
