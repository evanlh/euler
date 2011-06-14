"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

def n_primes(n):
	primes = [2]
	i =	max(primes) + 1 
	while len(primes) < n:
		for p in primes:
			if i % p == 0:
				break
		else:
			primes.append(i)
		i+=1
	return primes

if __name__ == "__main__":
	p =  n_primes(10001)
	print max(p)


