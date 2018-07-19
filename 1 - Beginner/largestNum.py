# Let's find the largest among 3 user entered numbers

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))

if(num1 >= num2):
	if(num1 >= num3):
		print(num1, " is the biggest number.")
	else: 
		print(num3, " is the biggest number.")
else:
	if(num2 >= num3):
		print(num2, " is the biggest number.")
	else: 
		print(num3, " is the biggest number.")	

