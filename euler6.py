""" Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sum_of_squares (nums):
	return sum(x**2 for x in nums)

def square_of_sums (nums):
	return sum(nums) ** 2


if __name__ == __main__:
	a, b =  square_of_sums (range(11)), sum_of_squares(range(11))
	print a, b, a - b

	a, b = square_of_sums (range(101)), sum_of_squares(range(101))
	print a, b, a - b
