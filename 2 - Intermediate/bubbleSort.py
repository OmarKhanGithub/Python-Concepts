# Simple Bubble sort
# @author: Omar Khan
# @version: 1.0
# @date: 30/07/18

# @Time complexity - Best:    Ω(n)
# @Time complexity - Average: O(n^2)
# @Time complexity - Worst:   O(n^2)
# @Space complexity:          O(1)


def bubbleSort(arr):

	# n will be the length of the array variable
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n): # in this case it would be 6

        # Last i elements are already in place
        for j in range(0, n-i-1): # 0->5, 0->4, 0->3 ...etc
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element 		

            if arr[j] > arr[j+1] :
            # if item 0 > item 1, switch their positions
            # running a second time follows the same rule HOWEVER...
            # ... the arr[j] is now the next element 
            # if its not bigger, arr j will move up using the forloop's
            # increment of the j variable 
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
bubbleSort(arr)


print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
