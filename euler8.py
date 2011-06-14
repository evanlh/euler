""" Find the greatest product five consecutive digits in the 1000-digit number found in euler8.txt """
import operator

if __name__ == "__main__":
	f = open(r"euler8.txt", 'r')
	num = ''
	for line in f:
		num += line.strip()

	i = 0
	maxnum = 0
	while len(num[i:i+5]) == 5:
		n = [int(x) for x in num[i:i+5]]
		maxnum = max(reduce(operator.mul, n), maxnum)
		i+=1

	print maxnum
