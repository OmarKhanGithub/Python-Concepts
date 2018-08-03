# Simple binary search

# Basic Linear/Sequential searching is just going through every element one by one
# The efficiency is O(n) time complexity
# Know whether the list is ordered or unordered

# Don't sort a large unsorted array, that time is better used for searching
# Unless you want to search many times...
# Binary Searchfficiency for worst/avg is O(log2*n)

arr = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
val = 42

def binary_search(arr, val):

	# Check if array is empty or the one item isn't the desired item
	if len(arr) == 0 or (len(arr)==1 and arr[0]!=val):
		return False
	
	# The center of the array
	mid = arr[len(arr)//2]
	
	if val==mid: return True
	if val<mid: return binary_search(arr[:(len(arr))//2], val)
	if val>mid: return binary_search(arr[(len(arr))//2+1:], val)
	
print(binary_search(arr, 41))

