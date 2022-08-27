
"""
This code runs in O(n) in the best case
The reason being, during the first iteration of the outer loop, if the inner loop doesn't find two 
consecutive elements to swap, the outer loop breaks after the first pass
"""
def read(filename):
    file = open("tests/" + filename, "r")
    First_line = file.readline()
    Second_line = file.readline().split(" ")
    for i in range(len(Second_line)):
        Second_line[i] = int(Second_line[i])
    b = []
    file.close()
    if len(b):
        for i in range(len(b)):
            b[i] = int(b[i])
        return Second_line
    return Second_line

def write(filename, content):
    file = open("tests/" + filename, "w")
    for elements in content:
        file.write(f"{elements} ")
    file.close()



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