from Stock import Stock

class Data:
	def __init__(self, stockList):
		self.stockList = stockList

	def sortPERatio(self):
		temp = self.stockList
		temp.sort(key=lambda x: x.peRatio, reverse=False)
		for x in temp:
			x.printInfo()
