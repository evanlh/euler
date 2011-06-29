""" More efficient solution to problem 12: What is the value of the first triangle number to have over five hundred divisors?"""

from math import sqrt, log
from euler10 import primes_sieve, sieve_between, primes_up_to
from operator import mul


def nth_triangle (n):
	""" Returns the nth triangle number."""
	accum = n
	while n > 0:
		n -= 1
		accum += n

	return accum

def triangles ():
	""" Yields an (index, triangle) tuple of triangle numbers and their corresponding index. Ex usage: for (index, triangle) in triangles():"""
	accum = 0
	i = 1
	while 1:
		accum += i
		yield i, accum
		i += 1


def num_divisors (n):
	""" Calculates the number of divisors of n, based on the fact that for a prime decomposition of n into (p1**v1)(p2**v2)..(pn**vn) the number of divisors is equivalent to (v1 + 1)(v2 + 1)..(vn + 1) """
	global PRIMES		# this is very poor form. best way to remove while maintaining performance? pass as argument?
	if abs(n) <= 3:
		return 1
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

	PRIMES  = primes_sieve(1000000) # get all primes < one million
	for (index, t) in triangles():
		count = num_divisors(t)
		if count >= 500:
			print index, t, count
			break

