""" The paths through a grid of size gridsize can be represented
	as a string of bits of length 2*gridsize, where 1 increments y
	and 0 increments x, and where there are always an even number of
	1's and 0's. The number of unique combinations of these paths is given
	by the combination formula, 2*gridsize taken gridsize at a time, or:
	(2*gridsize)! / (gridsize!)^2 """

from math import factorial
import sys
if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Usage: euler15.py gridsize"
		exit()

	gridsize = int(sys.argv[1])

	lenseq = 2 * gridsize
	numcombos = factorial(lenseq)/(factorial(gridsize))**2
	print "Number of paths: ", numcombos
