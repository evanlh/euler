"""Find the sum of all the primes below two million."""
from math import sqrt
import timeit
def primes_up_to(n):
	"""More efficient way of finding the primes below n"""
	primes = [2]
	i =	max(primes) + 1 
	halt = sqrt(n)
	while i <= n:
		for p in primes:
			if i % p == 0:
				break
			if p > halt:
				primes.append(i)
				break
		else:
			primes.append(i)
		i+=1
	return primes

def sieve_between(primes, minimum, maximum):
	""" Returns a sieved list of primes between minimum and maximum. Assumes
	primes is a sorted list of primes up to at least sqrt(maximum)"""

	halt = sqrt(maximum)
	sieve = dict([(x, 1) for x in range(minimum, maximum + 1)])
	for p in primes:
		sieve.update (dict([(p*x, None) for x in range(max(int(minimum/p), 2), int(maximum/p) + 1)]))
		if p > halt:
			break
	
	return [k for (k, v) in sieve.iteritems() if v is not None ]

def primes_sieve(n):
	""" Another method of finding primes up to n, works better for large n """

	primes = primes_up_to(int(sqrt(n))) # bootstrap
	chunk = 100000
	segments = [(max((x-1)*chunk, 2), min(x*chunk - 1, n)) for x in range(1, max(int(n / chunk) + 1, 2))]
	lotsoprimes = []
	for (a, b) in segments:
		lotsoprimes.extend(sieve_between(primes, a, b))
	return lotsoprimes


if __name__ == "__main__":
	print sum(primes_sieve (2000000))
	"""for i in range(1,100):
		stmt = "from euler10 import primes_sieve\nprimes_sieve(" + str(i * 100000) + ")"
		print i * 100000, timeit.Timer(stmt, 'gc.enable()').timeit(1)

	"""
