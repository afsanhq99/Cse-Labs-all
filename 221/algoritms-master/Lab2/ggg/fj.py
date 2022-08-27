def read(filename):
    file = open("tests/" + filename, "r")
    First_line = file.readline()
    Second_line = file.readline().split(" ")
    for i in range(len(Second_line)):
        Second_line[i] = int(Second_line[i])
    k = []
    file.close()
    if len(k):
        for i in range(len(k)):
            k[i] = int(k[i])
        return Second_line
    else:
        return Second_line

def write(filename, content):
    file = open("tests/" + filename, "w")
    for elements in content:
        file.write(f"{elements} ")
    file.close()

file=open("tests/task5(b)_input.txt", "r")
a=file.readline().split(" ")
for i in range(len(a)):
    a[i]=int(a[i])


k=read("task5(b)_input.txt")
arr=a

# Python3 implementation of randomized
# quickSelect
import random


# This function returns k'th smallest
# element in arr[l..r] using QuickSort
# based method. ASSUMPTION: ELEMENTS
# IN ARR[] ARE DISTINCT
def kthSmallest(arr, left, right, K=None):
    if K is None:
        K = [3, 5, 7]
    for i in K:

        if (left == right):
             return arr[left]
        pos = partition(arr, left, right)
        count = pos - left + 1
        if ( count == K ):
             return A[pos]
        elif ( count > i ):
             return kthSmallest(arr, left, pos-1, i)
        else:
             return kthSmallest(arr, pos+1, right, i)


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

    print("K'th smallest element is",
          kthSmallest(arr, 0, n - 1, k))

# This code is contributed by PranchalK
