"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def primes_up_to(n):
	""" Returns a list of all the prime numbers less than or equal to n. Brute-force, don't use for large n."""
	return [ x for x in range(2,n + 1) if sum([y for y in range(2, x) if x % y == 0]) == 0]

if __name__ == "__main__":
	""" my general approach: 1) find the maximum power of each prime that divides evenly into the dividers, thus avoiding a prime factor decomposition 3) multiply them together. """

	dividers = range(2,21) # everything is divisible by 1 so byebye
	primes = primes_up_to(20)
	result = {}
	for d in dividers:
		for p in primes:
			if p <= d:
				i = 1
				while d % (p**i) == 0:
					if p in result:
						if i > result[p]:
							result[p] = i
					else:
						result[p] = i

					i += 1
	print result

	i = 1
	for k in result:
		i *= k**result[k]

	print i
