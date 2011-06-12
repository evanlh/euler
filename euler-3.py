def min_even_divisor(num):
        i = 2
        while i <= num:
                if (num % i == 0):
                        return i
                i += 1

N = 600851475143
largest_prime = min_even_divisor(N)
print "N: ", N, ", largest prime: ", largest_prime
while (N != 1):
        N = N / largest_prime
        largest_prime = min_even_divisor(N)
        print "N: ", N, ", largest prime: ", largest_prime

