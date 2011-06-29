""" First brute-force attempt at a solution to problem 12, What is the value of the first triangle number to have over five hundred divisors? """

from math import sqrt, log

def nth_triangle (n):
	accum = n
	while n > 0:
		n -= 1
		accum += n

	return accum


def divisors (n):
	divs = [1]
	if n != 1:
		divs.append(n)

	i = 2
	while i <  sqrt(n):
		if n % i == 0:
			divs.append(i)
			divs.append(n / i)
		i += 1


	return divs


if __name__ == "__main__":

	i = 7
	count = 0
	while count < 500:
		t = nth_triangle(i)
		d = divisors(t)
		count = len(d)
		if count >= 500:
			print i, t, count, log(t)
		i += 1

