from Controller import Controller

def addStock():
	ticker = input("What ticker would you like to add?")

def printMenu():
	print("(0) for current portfolio")
	print("(1) to add stock")
	print("(2) to remove stock")
	print("(3) to check stock info")
	print("(q) to quit")

if __name__ == "__main__":
	controller = Controller()
	selection = ""

	while not selection == "q":
		printMenu()
		selection = input()
		if selection == "0":
			controller.printPortfolio()
		elif selection == "1":
			symbol = input("What is the symbol? ")
			companyName = input("What is the company name? ")
			costBasis = input("What is the total cost basis? ")
			shareCount = input("How many total shares in your account? ")
			controller.addStock(symbol, companyName, costBasis, shareCount)
		elif selection == "2":
			symbol = input("What is the symbol? ")
			controller.removeStock(symbol.upper())
		elif selection == "3":
			controller.printStockInfo()


