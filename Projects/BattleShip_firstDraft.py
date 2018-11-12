# Commenting is control shift M or Control M
# Or alternatively Shift 3

import random

# Initialize the Battle Ship Board Symbols
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

# Initialize the lists that will keep track of the coordinates of the ships
carrierLocation = []
battleShipLocation = []
cruiserLocation = []
submarineLocation = []
destroyerLocation = []

# List that will contain all the previously assigned coordinates
# As to not allow 2 ships to share any same position
locationTemp = []

# ------------------------------------------------------------------------------------------------------------------------------

# Making the board for the game!
def generateBoard():
	print("\n")
	print("     -------------------------------------")
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
					print('\n')
					sideCounter = sideCounter + 1
					print(sideCounter, end="", flush=True)
					if sideCounter > 9:
						print("   ", end="", flush=True)
					else:
						print("    ", end="", flush=True)
				print(i, end="", flush=True)
				print("   ", end="", flush=True) 
				counter = counter + 1
	
	print('\n')		
# Print the legend on the board to help the user learn what the symbols represent
	print('         ------------------------------')	
	print("                     Legend:")
	print("             □ = Unshot Board Target")
	print("             ▀ = Missed Shot")
	print("             X = Successful-Shot")
	print('         ------------------------------')

# ------------------------------------------------------------------------------------------------------------------------------

# Function to place the assigned ship randomly
def placeShip(x, y, ship):

# Allow the lists defined above to affect the global scope
	global carrierLocation
	global battleShipLocation
	global cruiserLocation
	global submarineLocation
	global destroyerLocation
	
	global locationTemp
	
	j = random.randint(0,999)
	
# If the random (0 - 9) value MINUS shipLength is LESS THAN zero, go UP from that value 
	if j <= 500:
		
		if (x - ship < 0): 
			def firstCheck(x,y,ship):
				for i in range(0,ship):
					if ship == 5:
						carrierLocation.append([x,y])
						x = x + 1
					elif ship == 4:
						battleShipLocation.append([x,y])
						x = x + 1
					elif ship == 3 and len(cruiserLocation) < 3 :
						cruiserLocation.append([x,y])
						x = x + 1
					elif ship == 3:
						submarineLocation.append([x,y])
						x = x + 1
					elif ship == 2:
						destroyerLocation.append([x,y])
						x = x + 1
			firstCheck(x,y,ship)
			
	# If the random (0 - 9) value PLUS shipLength is GREATER THAN 9, go DOWN from that value 
		elif(x + ship > 9):
			for i in range(0,ship):
				if ship == 5:
					carrierLocation.append([x,y])
					x = x - 1
				elif ship == 4:
					battleShipLocation.append([x,y])
					x = x - 1
				elif ship == 3 and len(cruiserLocation) < 3 :
					cruiserLocation.append([x,y])
					x = x - 1
				elif ship == 3:
					submarineLocation.append([x,y])
					x = x - 1
				elif ship == 2:
					destroyerLocation.append([x,y])
					x = x - 1
				
	# If the ship length plus/minus our random value stays in the range, then just go up
	# Can be changed to randomly MINUS too, consider doing this later.
		else:
			for i in range(0,ship):
				if ship == 5:
					carrierLocation.append([x,y])
					x = x + 1
				elif ship == 4:
					battleShipLocation.append([x,y])
					x = x + 1
				elif ship == 3 and len(cruiserLocation) < 3 :
					cruiserLocation.append([x,y])
					x = x + 1
				elif ship == 3:
					submarineLocation.append([x,y])
					x = x + 1
				elif ship == 2:
					destroyerLocation.append([x,y])
					x = x + 1
	else:
		if (y - ship < 0): 
			for i in range(0,ship):
				if ship == 5:
					carrierLocation.append([x,y])
					y = y + 1
				elif ship == 4:
					battleShipLocation.append([x,y])
					y = y + 1
				elif ship == 3 and len(cruiserLocation) < 3 :
					cruiserLocation.append([x,y])
					y = y + 1
				elif ship == 3:
					submarineLocation.append([x,y])
					y = y + 1
				elif ship == 2:
					destroyerLocation.append([x,y])
					y = y + 1
			
	# If the random (0 - 9) value PLUS shipLength is GREATER THAN 9, go DOWN from that value 
		elif(y + ship > 9):
			for i in range(0,ship):
				if ship == 5:
					carrierLocation.append([x,y])
					y = y - 1
				elif ship == 4:
					battleShipLocation.append([x,y])
					y = y - 1
				elif ship == 3 and len(cruiserLocation) < 3 :
					cruiserLocation.append([x,y])
					y = y - 1
				elif ship == 3:
					submarineLocation.append([x,y])
					y = y - 1
				elif ship == 2:
					destroyerLocation.append([x,y])
					y = y - 1
				
	# If the ship length plus/minus our random value stays in the range, then just go up
	# Can be changed to randomly MINUS too, consider doing this later.
		else:
			for i in range(0,ship):
				if ship == 5:
					carrierLocation.append([x,y])
					y = y + 1
				elif ship == 4:
					battleShipLocation.append([x,y])
					y = y + 1
				elif ship == 3 and len(cruiserLocation) < 3 :
					cruiserLocation.append([x,y])
					y = y + 1
				elif ship == 3:
					submarineLocation.append([x,y])
					y = y + 1
				elif ship == 2:
					destroyerLocation.append([x,y])
					y = y + 1
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
		if len(battleShipLocation) == 4:
			if battleShipLocation[0] in locationTemp or battleShipLocation[1] in locationTemp or battleShipLocation[2] in locationTemp  or battleShipLocation[3] in locationTemp:
				battleShipLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), battleship)
			else:
				locationTemp.append(battleShipLocation[0])
				locationTemp.append(battleShipLocation[1])
				locationTemp.append(battleShipLocation[2])
				locationTemp.append(battleShipLocation[3])
	
# Same checking feature here...with one caviat
# Cruiser and Submarine are both 3 blocks wide, we know the first one to be assigned
# will be cruiser, once its values are put in the list, make sure it doesn't use the
# submarine if statement by changing the ship size
	if ship == 3:	
		if len(cruiserLocation) == 3:
			if cruiserLocation[0] in locationTemp or cruiserLocation[1] in locationTemp or cruiserLocation[2] in locationTemp:
				cruiserLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), cruiser)

			else:
				locationTemp.append(cruiserLocation[0])
				locationTemp.append(cruiserLocation[1])
				locationTemp.append(cruiserLocation[2])
				ship = 6
				
# We add this placeholder so we don't confuse the request of the submarine coming
# next, submarine would enter the above statement since ship == 3 but the next one
# wouldn't work because len(cruiserLocation) is now 4 instead of 3, clever, right? :P
				cruiserLocation.append('PlaceHolder')
	
# The only if statement that Submarine would successfully go through			
	if ship == 3:
		if len(submarineLocation) == 3:
			if submarineLocation[0] in locationTemp or submarineLocation[1] in locationTemp or submarineLocation[2] in locationTemp:
				submarineLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), submarine)
			else:
				locationTemp.append(submarineLocation[0])
				locationTemp.append(submarineLocation[1])
				locationTemp.append(submarineLocation[2])

# Remember to remove the cruiser item because otherwise this list will become
# compromised for later use.
				cruiserLocation.remove('PlaceHolder')
			
# Normal check on the unique destroyer block
	if ship == 2: 
		if len(destroyerLocation) == 2:
			if destroyerLocation[0] in locationTemp or destroyerLocation[1] in locationTemp:
				destroyerLocation = []
				placeShip(random.randint(0,9), random.randint(0,9), destroyer)
			else:
				locationTemp.append(destroyerLocation[0])
				locationTemp.append(destroyerLocation[1])

# ------------------------------------------------------------------------------------------------------------------------------

def didItHit(x):
	target = input("\n\nWhere would you like to shoot Commander? [eg; B5 or b5] \t")

# Will contain the array value corresponding to the letter inputted by the user
	var = targetDict[target[0]]
# Will contain the array value corresponding to the number inputted by the user
	var2 = int(target[1])
# We must subtract one to make up for the battleship (1-10) scheme and the python
# array scheme that starts from zero instead of one (0-9)
	var2 = var2 - 1
	
# If the last value of the user inputted info is zero, system will assume that they meant 10
# which corresponds to 9 in the array scheme
	if target[-1] == '0':
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

# Prompting the user that battleships are now generated
print("BATTLE SHIPS GENERATED!")

# Intialize sizes for each style of battleship
carrier = 5
battleship = 4
cruiser = 3
submarine = 3
destroyer = 2

# Call function to place each of all the ships
placeShip(random.randint(0,9), random.randint(0,9), carrier)
placeShip(random.randint(0,9), random.randint(0,9), battleship)
placeShip(random.randint(0,9), random.randint(0,9), cruiser)
placeShip(random.randint(0,9), random.randint(0,9), submarine)
placeShip(random.randint(0,9), random.randint(0,9), destroyer)


# Let's cheat a bit, where exactly are the ships positioned
print("Carrier Location: ", carrierLocation)
print("Battleship Location: ", battleShipLocation)
print("Cruiser Location: ", cruiserLocation)
print("Submarine Location: ", submarineLocation)
print("Destroyer Location: ", destroyerLocation)
location = carrierLocation + battleShipLocation + cruiserLocation + submarineLocation + destroyerLocation

generateBoard()

# Dictionary of values translating the Coordinate into an array position value 
targetDict = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,
			  "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
			  
# Targets already shot, to compare to the list with the coordinates of
# the actual ships
pastTargets = []
x = True
x = 0
while True:
	x = didItHit(x)
	if x == 404:
		break
