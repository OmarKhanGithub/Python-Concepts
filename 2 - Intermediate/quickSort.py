# Simple Quick sort
# @author: Omar Khan
# @version: 1.0
# @date: 30/07/18

# @Time complexity - Best:    Ω(n log(n))
# @Time complexity - Average: O(n log(n)) --> (REAL)
# @Time complexity - Worst:   O(n^2)
# @Space complexity:          O(log(n))

# n(n-1 comparisions) log n (and have to divide the list log n times) comparisons


# in-place version, changes the order by swapping or replacing
# in place is faster for 50,000 elemnts or LESS

# potentially 2-3 times faster tahn other sorts

from random import randint

def create_array(size=10, max=50):
	# return an array that contains (size) elements that range from 0 to max
	return [randint(0, max) for _ in range(size)]
	

# lomuto partition scheme
# parameters are the array, and low and high integer indices
def partition(a,low,high): 
	# final pivot location will be i, or directly to the left of the range
	i=low-1
	
	# pivot will be last value in the range
	pivot=a[high]
	
	# iterate index value j, through all values within low and high
	for j in range(low,high):
		if a[j]<=pivot:
			i+=1
			a[i],a[j]=a[j],a[i]
			
	# on each iteration, if the current value is less than or equal to the 
	# pivot, we can then increment our pivot index i, and swap the values of 
	# i and j respectively
	a[i+1],a[high]=a[high],a[i+1]
	return i+1
	
	
def quicksort_inplace(a,low=0, high=None):
	if high==None:
	# now we can assume we are in the first call of the function
	# and we need to set the value of high manually
		high=len(a)-1
	if low<high:
	# if untrue, we are finished sorting the array
	# if true, use partition function
		p_idx=partition(a,low,high)
		#pivot index is the function result holder
		quicksort_inplace(a,low,p_idx-1)
		quicksort_inplace(a,p_idx+1, high)
		# two separate recursive calls
		# first is sorting the range between low and pivot
		# second is between pivot and high
		
a=create_array()
print("Unsorted:", a)
quicksort_inplace(a)
print("Sorted (IN-PLACE):    ", a)



print("-------------------")

def quicksort(b):
	if len(b)<=1: return b
	# return array because a 1 element array is already sorted
	smaller, equal, larger=[],[],[]
	# create lists
	pivot = b[randint(0, len(b)-1)]
	# the pivot will be a random number in the input array
	
	# iterate over each element in array
	# append to appropriate list when comparing to the pivot
	for x in b:
		if x<pivot:	
			smaller.append(x)
		elif x==pivot:
			equal.append(x)
		else:
			larger.append(x)
	return quicksort(smaller)+equal+quicksort(larger)


b=create_array()
print("Unsorted:", b)

print("Sorted (NORMAL QUICKSORT):    ", quicksort(b))
