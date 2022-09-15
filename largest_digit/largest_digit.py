"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# We need to use helper function to find_the_largest_digit
	return find_largest_digit_helper(n,num=1,lastn=1)


def find_largest_digit_helper(n,num,lastn):

	# we need to let the number be positive
	if n <= 0:
		n = n*(-1)
	# The first number
	if n % 10 == 0:
		return num
	else:
	# The last number
		lastn = n % 10
	# The number is bigger than original we need to replace
		if lastn > num:
			num = lastn
	# The next last number
			n = n//10
			return find_largest_digit_helper(n, num,lastn)
		else:
			num = num
			n = n//10
			return find_largest_digit_helper(n, num,lastn)






if __name__ == '__main__':
	main()
