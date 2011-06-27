from math import sqrt

def nth_triangle (n):
	accum = n
	n -= 1
	while n > 0:
		accum += n
		n -= 1

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
		count = len(divisors(t))
		print i, t, count
		i += 1

