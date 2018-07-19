# Basic recursion program

def recursive(n):

	if n == 1:
	# Base case
		print(n)
		return 1
	else:
	# Recursive case
		print(n)
		return recursive(n-1)

recursive(5)
