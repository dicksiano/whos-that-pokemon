import random

def generateList():
	numLow = 0
	numHigh = 149

	listOfNumbers = []

	for x in range (0, 5):
	    listOfNumbers.append(random.randint(numLow, numHigh))

	return listOfNumbers
