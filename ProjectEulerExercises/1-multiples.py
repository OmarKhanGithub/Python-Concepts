saveList = []
def sumFunc(n):
	counter = 0
	while counter < n:
		if counter % 3 == 0 or counter % 5 == 0:
			saveList.append(counter)
		counter = counter + 1
	return sum(saveList)
print(sumFunc(1000))

# One line solution
# print(sum([i for i in range(1000) if i%3==0 or i%5==0]))
