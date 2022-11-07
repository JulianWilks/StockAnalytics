from Stock import Stock
from GetData import GetData
from Data import Data
import glob
import os

class Controller:
	def __init__(self):
		print("Controller Initiated")
		getdata = GetData()
		stockList = getdata.retData()
		self.data = Data(stockList)
		self.data.sortPERatio()
		#self.portfolio = Portfolio(data)


	def printDataInfo(self):
		print("poop")
		#self.data.getPE()


	def printStockInfo(self):
		for x in self.data.stockList:
			x.printInfo()

