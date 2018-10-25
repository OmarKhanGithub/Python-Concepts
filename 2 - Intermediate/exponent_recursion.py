def exp(x, n):
	if n == 0:
		return 1
	else:
		return x * exp(x, n-1)	


print(exp(5,2))	
