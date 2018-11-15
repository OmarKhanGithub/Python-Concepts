# ======================================================================================
# Battleship Program
# @version 1.0
# @author: Omar Khan
# @date: 11/11/18
# ======================================================================================

import random

"""Initialize the Battleship Board Symbols"""

battleShipBoard = [["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
			  	   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"],
				   ["□","□","□","□","□","□","□","□","□","□"]]

def generateBoard():
	"""Make the main board"""
	print("\n     -------------------------------------")
	print("     ------------ BATTLE SHIP ------------")
	print("     -------------------------------------\n")
	print("     A   B   C   D   E   F   G   H   I   J", end="", flush=True)
	counter = 0
	sideCounter = 0
	
	for x in battleShipBoard:
		for i in x:
				# Every 10 Squares, start a new line and print the remaining squares on
				# the next line until we reach another 10 and start a new line again
				if counter % 10 == 0:
					print("\n")
					sideCounter = sideCounter + 1
					print(sideCounter, end="", flush=True)
					if sideCounter > 9:
						print("   ", end="", flush=True)
					else:
						print("    ", end="", flush=True)
				print(i, end="", flush=True)
				print("   ", end="", flush=True) 
				counter = counter + 1
	
	# Print the legend on the board to help the user learn what the symbols represent
	print("\n\n         ------------------------------")	
	print("                     Legend:")
	print("             □ = Unshot Board Target")
	print("             ▀ = Missed Shot")
	print("             X = Successful-Shot")
	print("         ------------------------------")

def firstCheck(x,y,ship,route):
	"""Determine the coordinates of the ships to make sure its placed entirely on the board"""
	for i in range(0,ship):
		if ship == 5:
			carrierLocation.append([x,y])
			if route == "x_plus":	x = x + 1 # X-val assigned in increasing order - vertical
			if route == "x_minus":	x = x - 1 # X-val assigned in descending order - vertical
			if route == "y_plus":	y = y + 1 # Y-val assigned in increasing order - horizontal
			if route == "y_minus":	y = y - 1 # Y-val assigned in decreasing order - horizontal
		elif ship == 4:
			battleShipLocation.append([x,y])
			if route == "x_plus":	x = x + 1
			if route == "x_minus":	x = x - 1
			if route == "y_plus":	y = y + 1
			if route == "y_minus":	y = y - 1
		elif ship == 3 and len(cruiserLocation) < 3 :
			cruiserLocation.append([x,y])
			if route == "x_plus":	x = x + 1
			if route == "x_minus":	x = x - 1
			if route == "y_plus":	y = y + 1
			if route == "y_minus":	y = y - 1
		elif ship == 3:
			submarineLocation.append([x,y])
			if route == "x_plus":	x = x + 1
			if route == "x_minus":	x = x - 1
			if route == "y_plus":	y = y + 1
			if route == "y_minus":	y = y - 1
		elif ship == 2:
			destroyerLocation.append([x,y])
			if route == "x_plus":	x = x + 1
			if route == "x_minus":	x = x - 1
			if route == "y_plus":	y = y + 1
			if route == "y_minus":	y = y - 1

def addShipToCoordinatePool(shipLocation, ship, version):
	"""Append the coordinates of the ships to a list with all the coordinates"""

	global carrierLocation
	global battleShipLocation
	global cruiserLocation
	global submarineLocation
	global destroyerLocation
	
	global locationTemp

	if len(shipLocation) == ship:
		if any(x in locationTemp for x in shipLocation):
			if ship == 4 and version == 1:
				battleShipLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), battleship, 1)		
			if ship == 3 and version == 1:
				cruiserLocation = [] 
				placeShip(random.randint(0,9), random.randint(0,9), cruiser, 1)	
			if ship == 3 and version == 2:
				submarineLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), submarine, 2)	
			if ship == 2 and version == 1:
				destroyerLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), destroyer, 1)			
		else:
			for x in range(0, len(shipLocation)):
				locationTemp.append(shipLocation[x])

def placeShip(x, y, ship, model):
	"""Function to place the assigned ship randomly"""
	
	# Allow the lists defined above to affect the global scope
	global carrierLocation
	global battleShipLocation
	global cruiserLocation
	global submarineLocation
	global destroyerLocation
	
	global locationTemp
	j = random.randint(0,999)
	
	# If the random (0 - 9) value MINUS shipLength is LESS THAN zero, go UP from that value 
	# If the random (0 - 9) value PLUS shipLength is GREATER THAN 9, go DOWN from that value

	if j >= 500:
		"""There will be a 50% chance that the ship will be placed either"""
		"""vertically or horizontally"""
		if(x + ship > 9):
			route = "x_minus"
			firstCheck(x,y,ship,route)
		else:
			route = "x_plus"
			firstCheck(x,y,ship,route)
	else:
		if(y + ship > 9):
			route = "y_minus"
			firstCheck(x,y,ship,route)
		else:
			route = "y_plus"
			firstCheck(x,y,ship,route)

	# Once the chosen ship has its coordinates in its list, we now must check what the 
	# dimensions of the ship are to identify which it is.
	# Then put its coordinates in a larger list of coordinates
	if ship == 5:
		if len(carrierLocation) == 5:
			locationTemp.append(carrierLocation[0])
			locationTemp.append(carrierLocation[1])
			locationTemp.append(carrierLocation[2])
			locationTemp.append(carrierLocation[3])
			locationTemp.append(carrierLocation[4])
		
	# Continue to check if the assigned position coordinates are in the larger list of
	# coordinates, if we have stumbled on a value already in the list of values, start
	# from scratch and assign new values that hopefully don't match
	if ship == 4:
		addShipToCoordinatePool(battleShipLocation, 4, 1)
	
	if ship == 3 and model == 1:		
		addShipToCoordinatePool(cruiserLocation, 3, 1)
				
	if ship == 3 and model == 2:
		addShipToCoordinatePool(submarineLocation, 3, 2)

	if ship == 2: 
		addShipToCoordinatePool(destroyerLocation, 2, 1)

def didItHit(x):
	target = input("\n\nWhere would you like to shoot Commander? [eg; B5 or b5] \t")
	
	# Will contain the array value corresponding to the letter inputted by the user
	var = targetDict[target[0]]
	# Will contain the array value corresponding to the number inputted by the user
	var2 = int(target[1])
	# B10 shouldn't refer to the 10th array element denoted by the number 9
	var2 = var2 - 1

	# Assume any coordinate ending in '0' is 10
	if target[-1] == "0":
		var2 = 9
		
	# Append the coordinates corresponding to the users target, to the pastTarget array
	item = [var, var2]
	pastTargets.append(item)
	
	# If the coordinates of the users target match any of those existing in the location list
	# which corresponds to ship coordinates, then indicate a hit, otherwise a miss
	if item in location:
		battleShipBoard[var2][var] = "X"
		print("HIT!")
	else:
		battleShipBoard[var2][var] = "▀"
		print("Miss!")

	generateBoard()

	# A check to see if all the items in Location, match the items in the Past Targets
	# If they do, that means we've hit all the targets and we've won!
	result =  all(elem in pastTargets for elem in location)
	x = 50
	if result:
		print("\n♠♡♣♢ ★☆★☆★☆★☆★☆★ YOU WIN! ☆★☆★☆★☆★☆★☆★ ♠♡♣♢\n")
		x = 404
		return x
	else:
		x = 50
		return x
		
# Initialize the lists that will keep track of the coordinates of the ships
carrierLocation = []
battleShipLocation = []
cruiserLocation = []
submarineLocation = []
destroyerLocation = []

# List that will contain all the previously assigned coordinates
# As to not allow 2 ships to share any same position
locationTemp = []

# Prompting the user that battleships are now generated
print("BATTLE SHIPS GENERATED!")

# Intialize sizes for each style of battleship
carrier = 5
battleship = 4
cruiser = 3
submarine = 3
destroyer = 2

# Call function to place each of all the ships
placeShip(random.randint(0,9), random.randint(0,9), carrier, 1)
placeShip(random.randint(0,9), random.randint(0,9), battleship, 1)
placeShip(random.randint(0,9), random.randint(0,9), cruiser, 1)
placeShip(random.randint(0,9), random.randint(0,9), submarine, 2)
placeShip(random.randint(0,9), random.randint(0,9), destroyer, 1)

# Let's cheat a bit, where exactly are the ships positioned
print("Carrier Location:    ", carrierLocation)
print("Battleship Location: ", battleShipLocation)
print("Cruiser Location:    ", cruiserLocation)
print("Submarine Location:  ", submarineLocation)
print("Destroyer Location:  ", destroyerLocation)
location = carrierLocation + battleShipLocation + cruiserLocation + submarineLocation + destroyerLocation

generateBoard()

# Dictionary of values translating the Coordinate into an array position value 
targetDict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
			  "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
			  
# Targets already shot, to compare to the list with the coordinates of the actual ships
pastTargets = []
x = True
x = 0
while True:
	x = didItHit(x)
	if x == 404:
		break
