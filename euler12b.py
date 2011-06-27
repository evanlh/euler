""" Slightly more efficient solution to problem 12: What is the value of the first triangle number to have over five hundred divisors?"""

from math import sqrt, log
from euler10 import primes_sieve, sieve_between, primes_up_to
from operator import mul

PRIMES  = primes_sieve(1000000) # get all primes < one million

def nth_triangle (n):
	accum = n
	while n > 0:
		n -= 1
		accum += n

	return accum

def num_divisors (n):
	halt = sqrt(n)
	divs = dict()
	for p in PRIMES:
		if p >= halt:
			break
		power = 1
		while n % (p ** power) == 0:
			divs[p] = power
			power += 1

	return reduce(mul, [v + 1 for (k, v) in divs.iteritems()])


if __name__ == "__main__":

	i, count = 7, 0
	while count < 500:
		triangle = nth_triangle (i)
		count = num_divisors(triangle)
		if count >= 500:
			print i, triangle, count
		i += 1

