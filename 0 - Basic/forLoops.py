myList = [1,2,3]


for i in range(5):
	print("FIRST LOOP!")

for x in range(0, 5):
	print("SECOND LOOP!")

for j in myList:
	print("THIRD LOOP!")

for item in myList:
	print("FOURTH LOOP!")
	if(item == 2):
		break

for t in range(0, 10, 2):
	print(t, "FIFTH LOOP!")

