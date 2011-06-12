def fib(stop_at = 0):
        a, b = 0, 1
        while a <= stop_at and stop_at > 0:
                yield a
                a, b = b, a + b

print sum([x for x in fib(4000000) if x % 2 == 0])
