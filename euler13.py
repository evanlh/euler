if __name__ == "__main__":
	f = open('euler13.txt', 'r')
	accum = long(0)
	for line in f:
		accum += long(line)

	print accum
	print str(accum)[0:10]
