class node: #subclass of linkedlist

# A class is an exact blueprint for individual objects with exact behaviour

	def __init__(self,data = None): 

#__init__ is a method in python classes and a constructor, its called
# when an object is created is created from the class
# it allows us to initialize the attributes of the class

		self.data = data # the self represents the instance of the class
		self.next = None # the pointer initially points to nothing
	
class linked_list:
	
	def __init__(self):
		self.head = node() # placeholder to point to first element in list

	def append(self, data): 
		new_node = node(data) # set the data point inside the node
		cur = self.head # looking at the left most point of the list
		while cur.next != None: # while the next position has something in it
			cur = cur.next # Our current node will become the next node
		cur.next = new_node # when that stops, the new data will be at the next spot

	def length(self): # only parameter is the instance of the class
		cur = self.head
		total = 0 # number of nodes seen
		while cur.next != None:
			total+=1
			cur = cur.next # Once this all runs and finishes, total will contain the length
		return total
	
	def display(self):
		elems = [] 
		cur_node = self.head # the current node
		while cur_node.next != None: # traversing over the nodes
			cur_node = cur_node.next # cureent is now next node
			elems.append(cur_node.data) # append current node to list of elements
		print (elems)
		
	def get(self, index):
		if index >= self.length(): # check if user inputted index is not out of range
			print("ERROR!")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx==index: # we are now at the data point we wish to extract
				return cur_node.data
			cur_idx+=1
			
	def erase(self, index):
		if index>=self.length():
			print("ERROR!")
			return 
		cur_idx = 0 # initialize
		cur_node=self.head # cur_node is the first one
		while True:
			last_node = cur_node # when erasing a node, like 3, after erasing it, points to the appropriate spot, id 2, is 4
			cur_node = cur_node.next
			if cur_idx==index: # check if we're at the index user provided
				last_node.next = cur_node.next # just change the pointer = erasing current nodes
				return
			cur_idx+=1 # we have incremented current node
	

my_list = linked_list() # create instance
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.erase(1)
my_list.display()
print("Element at 2nd index: %d" % my_list.get(2))
