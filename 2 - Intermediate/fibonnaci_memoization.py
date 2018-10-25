memoization_cache = {}

def fibonnaci(n):
	if n in memoization_cache:
		return memoization_cache[n] 
	# this is so the recursive function saves a repeat number
	# and return the fib value for other things
		
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonnaci(n-1) + fibonnaci(n-2)

	memoization_cache[n] = value
	return value 
	# if it gets to this point, the value is not a repeat
	# save the value to the cache

for n in range(1,101):
	print(n, ":", fibonnaci(n))
