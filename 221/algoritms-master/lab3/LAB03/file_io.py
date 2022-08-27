"""
All the tasks in this lab invokes the read function and read input from file
and invoke the write function to write output to designated file
"""

# Python3 implementation of randomized
# quickSelect
import random

# This function returns i'th smallest
# element in arr[l..r] using QuickSort
# based method. ASSUMPTION: ELEMENTS
# IN ARR[] ARE DISTINCT
arr=[1,2,3,4,5,6,7]
k=[3,4,5]
def kthSmallest(arr, l, r):
	
	# If i is smaller than number of
	# elements in array
    k=[3,4,5]
    for i in k:
        if (i > 0 and i <= r - l + 1):
            
            # Partition the array around a random
            # element and get position of pivot
            # element in sorted array
            pos = randomPartition(arr, l, r)

            # If position is same as i
            if (pos - l == i - 1):
                return arr[pos]
            if (pos - l > i - 1): # If position is more,
                                # recur for left subarray
                return kthSmallest(arr, l, pos - 1)

            # Else recur for right subarray
            return kthSmallest(arr, pos + 1, r,
                            )

        # If i is more than the number of
        # elements in the array
        return 999999999999

def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it and
# greater elements to right. This function
# is used by randomPartition()
def partition(arr, l, r):
	x = arr[r]
	i = l
	for j in range(l, r):
		if (arr[j] <= x):
			swap(arr, i, j)
			i += 1
	swap(arr, i, r)
	return i

# Picks a random pivot element between l and r
# and partitions arr[l..r] around the randomly
# picked element using partition()
def randomPartition(arr, l, r):
	n = r - l + 1
	pivot = int(random.random() * n)
	swap(arr, l + pivot, r)
	return partition(arr, l, r)

# Driver Code
if __name__ == '__main__':

	arr = [12, 3, 5, 7, 4, 19, 26]
	n = len(arr)
	itst = k
	print("K'th smallest element is",
		kthSmallest(arr, 0, n - 1))
