#
# Simple Binary Search Tree Structure
# @version 1.0
# @author: Omar Khan
# @tutorial from: https://www.youtube.com/watch?v=f5dU3xoE6ms 
# @date: 29/07/18
#


class node:
	def __init__(self, value=None):
	# constructor
	# user never directly interacts with this
	# when making a node, dont assume it has child nodes already
	
		self.value=value
		self.left_child=None
		self.right_child=None
		
	# the wrapper that manages all the node classes
class binary_search_tree:
	
	# class's constructor
	def __init__(self):
	
		# root will be the parent of the node
		self.root=None
		
	def insert(self, value):
	
		# insert the value at the root (first node)
		if self.root==None:
			# the root will become the value if no root already exists
			self.root=node(value)
		else:
			self._insert(value, self.root)
			# insert the value with respect to the root node
			# _ means don't call this function outside of class, private function
			# lets make a second insert function because we want one without recursion
			
	def _insert(self, value, cur_node):
			# check if the value is less than the current/root node
		if value<cur_node.value: 
			if cur_node.left_child==None:
			# then the new left child will be that new value
				cur_node.left_child=node(value)
			else:
			# if it already has a left child, then recurse on the left node
				self._insert(value, cur_node.left_child)
				
			# if the value is bigger than the current node
			# make the value node the new right child
			# if it already exists, recurse it again
		elif value> cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
			else:
				self._insert(value, cur_node.right_child)
				
		else:
			print("Value already in tree!")
			
	def print_tree(self):
		# checking if the root exists
		if self.root!=None:
		# start recursing using the root as input
			self._print_tree(self.root)
			
			
			
		# non-recursive function that traverses the tree 
		# in a complete sorted order
	def _print_tree(self, cur_node):
		# if the curernt node exists
		if cur_node!= None:
		
		# current node will now be equal to the left child and be printed
			self._print_tree(cur_node.left_child) 
			print(str(cur_node.value))
		# current node will now be equal to the right child and be printed
			self._print_tree(cur_node.right_child)
			
	def height(self):
	
		# if a root node exists
		if self.root!=None:
			# feed the node into the private function
			return self._height(self.root, 0)
		else:
			return 0 
			
	def _height(self, cur_node, cur_height):
		# if the node doesn't exist, return the 0 height passed in
		if cur_node==None: return cur_height
		# the height of the left and right sub tree and then compare which is bigger 
		left_height=self._height(cur_node.left_child, cur_height+1)
		right_height=self._height(cur_node.right_child, cur_height+1)
		# return whichever is bigger, 
		return max(left_height, right_height)
		
		# enter desired value
	def search(self, value):
		if self.root!=None:
			# pass the value and the root if it exists
			return self._search(value, self.root)
		else:
			return False
			
	def _search(self, value, cur_node):
		# check if our target is just the root node
		if value==cur_node.value:
			return True
		# if not, check if the value is less than the root (left child)
		elif value<cur_node.value and cur_node.left_child != None:
			return self._search(value, cur_node.left_child)
		# if not, check if the value is more than the root (right child)
		elif value>cur_node.value and cur_node.right_child != None:
			return self._search(value, cur_node.right_child)
		# can't find it
		else:
			return False


# insert random elements into the binary search tree
def fill_tree(tree, num_elems=100, max_int=1000):
	from random import randint
	for _ in range(num_elems):
		cur_elem = randint(0, max_int)
		tree.insert(cur_elem)
	return tree

tree = binary_search_tree()
#tree = fill_tree(tree)


# insert particular values into the tree
tree.insert(10)
tree.insert(7)
tree.insert(13)
tree.insert(9)
tree.insert(11)
tree.insert(5)
tree.insert(6)
tree.insert(12)

# show the tree values
tree.print_tree()

print (tree.search(10))
print (tree.search(20))

print("Tree height:" + str(tree.height()))
