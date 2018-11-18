# Is it prime?

def primeChecker(n):
	tempList = []
	for x in range(1, n+1):
		if n % x == 0:
			tempList.append(x)
	if len(tempList) < 3:
		print("Prime!")
		print(tempList)
	else:
		print("Not Prime!")
		print(tempList)

primeChecker(7)
primeChecker(10)
