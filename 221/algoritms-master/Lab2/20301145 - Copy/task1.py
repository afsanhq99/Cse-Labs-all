
"""
This code runs in O(n) in the best case
The reason being, during the first iteration of the outer loop, if the inner loop doesn't find two 
consecutive elements to swap, the outer loop breaks after the first pass
"""
from file_io import read,write 



def bubble_sort(arr):
    for i in range(len(arr) - 1):
        next_index = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                next_index = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if  next_index is None:
            break


a = read("task1_input1.txt")
bubble_sort(a)
write("task1_output1.txt", a)

b = read("task1_input2.txt")
bubble_sort(b)
write("task1_output2.txt", b)