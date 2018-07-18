# Area for a triangle program
# Need hight and base length

height = int(input("Enter the height of the triangle: "))
base = int(input("Enter the base of the triangle: "))

def triangleArea(height, base):
	area = (base * height)/2
	return area

x = triangleArea(height, base)
print("The area of the triangle would be", x)
