""" Find the Pythagorean triplet (a^2 + b^2 = c^2) for which a + b + c = 10000 """
def test(a, b, c):
	if a + b + c == 1000 and a**2 + b**2 == c**2:
		return True
	else:
		return False

if __name__== "__main__":
	c, b, a = 1000, 1000, 1000
	while c > 0 and not test(a, b, c):
		c-=1
		b = c-1
		while b > 0 and not test(a, b, c):
			b-=1
			a = b-1
			while a > 0 and not test (a, b, c):
				a-=1
	
	print a, b, c
