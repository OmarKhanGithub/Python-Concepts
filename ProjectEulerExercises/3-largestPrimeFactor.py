#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import time

primes = []
start_time = time.time()
def primeFactor(n):
	for x in range(2, n+1): # run through all the numbers between 1 and 20
		if n % x == 0: # 20 mod x would be 0 for 1,2,4,5,10,20
			temp = []
			for y in range(2, x): # for every value between 1 and 4 assuming x = 4
				if x % y == 0: # if 4 mod 2 = 0 because 2 is not 1 or 4, append all factors
					temp.append(y)
			if len(temp) < 1: # if there are less than 3 factors, its prime!
				primes.append(x)
				
	print(max(primes))
primeFactor(600851475143)
print("--- %s seconds ---" % (time.time() - start_time))

