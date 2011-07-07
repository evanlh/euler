def chain(n):
	i = 0
	while n > 1:
		if n % 2 == 0:
			n = n >> 1 """ bit shift division makes me happy"""
		else:
			n = 3*n + 1
		i += 1
	return i


if __name__ == "__main__":
	i = 1000000
	maximum = 0
	maxindex = 0
	while i > 0:
		c = chain(i)
		if c > maximum:
			maximum = c
			maxindex = i
		i -= 1

	print maxindex, maximum
