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


def partition(A,p,r):
    pivot_index = p
    pivot = A[pivot_index]
    while p < r:
        while p < len(A) and A[p] <= pivot:
            p += 1
        while A[r] > pivot:
            r -= 1
        if(p < r):
            A[p], A[r] = A[r], A[p]
    A[r], A[pivot_index] = A[pivot_index], A[r]
    return r

def quick_sort(A,p,r):
    if (p < r):
        r = partition(A,p, r)
        quick_sort(A,p,r - 1)
        quick_sort(A,r + 1, r)
# A = [ 10, 7, 8, 9, 1, 5 ]
# quick_sort(A,0, len(A) - 1)
arr=read("task5_input.txt")
part=partition(arr,0, len(arr)-1)


d=quick_sort(arr,0,part)
e=quick_sort(arr,part+1,len(arr)-1)
sort=arr
write("task5_output.txt",sort)
