class Stock:
	def __init__(self, info):#, currentPrice):
		print(info)
		self.symbol = info['symbol']
		self.companyName = info['longName']
		if 'trailingPE' in info:	
			self.peRatio = info['trailingPE']
		self.pbRatio = info['priceToBook']
		self.volume =  info['volume']
		self.ask = info['ask']
		self.fiftyDayAverage = info['fiftyDayAverage']
	'''
	def addData(self, companyName, openPrice, closePrice, high, low, volume, week52High, week52Low, peRatio):
		self.companyName = companyName
		self.open = openPrice
		self.close = closePrice
		self.high = high
		self.low = low
		self.volume = volume
		self.week52High = week52High
		self.week52Low = week52Low
		self.peRatio = peRatio
		self.hasData = True
	'''
	def printInfo(self):
		#print(self.symbol + " " + self.companyName + " " + str(self.peRatio) + " " + str(self.fiftyDayAverage) + " " + str(self.ask))
		print(self.symbol)
		print(self.companyName)
		if self.peRatio:
			print(self.peRatio)
		print('\n')