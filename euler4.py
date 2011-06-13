"""Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome (num):
	""" Returns boolean indicating whether num is a palindrome."""
        s = str(num)
        l = len(s) / 2
        return s[:l] == s[-l:][::-1]


if __name__ == "__main__":
	max = 0
	for a in range(0,999)[::-1]:
	        for b in range(0,999)[::-1]:
	                if is_palindrome (a * b):
	                        if a * b > max:
	                                max = a * b
	
	print max
