from operator import mul

if __name__ == "__main__":
	nums = []
	fo = open('euler11.txt', 'r')
	for line in fo:
		nums.append([int(x) for x in line.split(' ')])

	print nums

	maximum = 0
	i = 0
	while i < len(nums) - 3:
		j = 0
		while j < len(nums[i]) - 3:
			across = reduce(mul, nums[i][j:j + 3])
			down = reduce(mul, [nums[i][j], nums[i+1][j], nums[i+2][j], nums[i+3][j]])
			diag = reduce(mul, [nums[i][j], nums[i+1][j+1], nums[i+2][j+2], nums[i+3][j+3]])
			maximum = max(maximum, across, down, diag)
			j += 1
		i += 1

	# upward diagonals
	i = 3
	while i < len(nums) - 1:
		j = 0
		while j < len(nums[i]) - 3:
			updiag = reduce(mul, [nums[i][j], nums[i-1][j+1], nums[i-2][j+2], nums[i-3][j+3]])
			maximum = max(maximum, updiag)
			j += 1
		i += 1

	print maximum

