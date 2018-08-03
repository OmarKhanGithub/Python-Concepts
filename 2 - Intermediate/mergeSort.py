# Simple Merge Sort
# @author: Omar Khan
# @version: 1.0
# @date: 30/07/18

# @Time complexity - Best:    Ω(n log(n))
# @Time complexity - Average: O(n log(n))
# @Time complexity - Worst:   O(n log(n))
# @Space complexity:          O(n)

# Break array into chunks
# DIVIDE AND CONQUER!
# Not in place
# Sorts the chunks individually and makes a new partition using the sorted chunk
# elements sequentially

def create_array(size=10, max=50):
	from random import randint
	return [randint(0,max) for _ in range(size)]
	
# combine our two separate arrays
def merge(a,b):
	# create a list or final output array 
	c=[]

	# a and b index will be intialized to 0 representing first array elements
	a_idx, b_idx=0,0
	
	# while these variables are less than the length of the lists
	# so we can iterate [list items] number of times
	while a_idx<len(a) and b_idx<len(b):
		
		# check if each element is less than the same index element in the
		# other array
		if a[a_idx]<b[b_idx]:
		# if it is less, then add that lesser item to the c list 
			c.append(a[a_idx])
			a_idx+=1 # increment the index array because we are done with it 
		else:
		# if it is more, then 
			c.append(b[b_idx])
			b_idx+=1
	if a_idx==len(a): 
		c.extend(b[b_idx:]) # done when all items processed from a
					# remaining b elemnts must then be appended to c
	else:			  
		c.extend(a[a_idx:]) # if a_idx!=len(a), just append whatever
					# is left from c
	return c
	
def merge_sort(a):
	
	#array of 1 item is already sorted
	if len(a)<=1: return a
	
	# create a left and right side which contains half the array respectively
	left,right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
	
	# return the array
	return merge(left,right)
	

a=create_array()
print(a)
s=merge_sort(a)
print(s)	
			
#a=[1,3,5]
#b=[2,4,6]
#print(merge(a,b))
#print(merge_sort(a))
