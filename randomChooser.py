import random

def generateList():
	numLow = 1
	numHigh = 150

	listOfNumbers = []

	for x in range (0, 5):
	    listOfNumbers.append(random.randint(numLow, numHigh))

	return listOfNumbers
