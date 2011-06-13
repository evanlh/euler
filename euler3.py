""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def min_even_divisor(num):
	""" Finds the minimum number >= 2 that evently divides num"""
        i = 2
        while i <= num:
                if (num % i == 0):
                        return i
                i += 1

if __name__ == "__main__":
	N = 600851475143
	largest_prime = min_even_divisor(N)
	print "N: ", N, ", largest prime: ", largest_prime
	while (N != 1):
	        N = N / largest_prime
	        largest_prime = min_even_divisor(N)
	        print "N: ", N, ", largest prime: ", largest_prime
	
