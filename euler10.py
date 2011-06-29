"""Find the sum of all the primes below two million."""
from math import sqrt
def primes_up_to(n):
	"""Somewhat efficient way of finding the primes up to n for small n"""
	primes = [2]
	i =	max(primes) + 1 
	halt = sqrt(n)
	while i <= n:
		for p in primes:
			if i % p == 0:
				break
			if p >= halt:
				primes.append(i)
				break
		else:
			primes.append(i)
		i+=1
	return primes

if __name__ == "__main__":
	print sum(primes_up_to(2000000))

