saveList = []

def sumFunc(n):
	counter = 0
	while counter < n:
		if counter % 3 == 0 or counter % 5 == 0:
			print(counter)
			saveList.append(counter)
		counter = counter + 1
	return sum(saveList)
			
print(sumFunc(1000))
