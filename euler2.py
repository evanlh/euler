"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

def fib(stop_at = 0):
        a, b = 0, 1
        while a <= stop_at and stop_at > 0:
                yield a
                a, b = b, a + b

if __name__ == "__main__":
	print sum([x for x in fib(4000000) if x % 2 == 0])
