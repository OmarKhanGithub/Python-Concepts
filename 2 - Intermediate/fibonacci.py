
# Omar Khan
# Fibonnaci Program

def fibonnaci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonnaci(n-1) + fibonnaci(n-2)

for n in range(1,40):
	print(n, ":", fibonnaci(n))
	
#def fibonnaci(n)
#	nums = []
#	nums[0] = 1
#	nums[1] = 1
#	while (True):
#		nums[n] = 
# ----------------------------------------------
#def recur_fibo(n):
#   """Recursive function to
#   print Fibonacci sequence"""
#   if n <= 1:
#       return n
#   else:
#       return(recur_fibo(n-1) + recur_fibo(n-2))
       
# if n = 4
# return fib(3) + fib(2) = 2 + 1 = 3
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
# fib(2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(1) = 1 & fib(0) = 0

#print(recur_fibo(4))


