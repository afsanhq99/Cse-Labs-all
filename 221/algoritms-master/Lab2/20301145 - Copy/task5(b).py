from file_io import *

file=open("tests/task5(b)_input.txt", "r")
a=file.readline().split(" ")
for i in range(len(a)):
    a[i]=int(a[i])
print(read("task5(b)_input.txt"))
main=a
print(main)


def partition(A, p, r):
    pivot_index = p
    pivot = A[pivot_index]
    while p < r:

        while p < len(A) and A[p] <= pivot:
            p += 1

        while A[r] > pivot:
            r -= 1

        if (p < r):
            A[p], A[r] = A[r], A[p]

    A[r], A[pivot_index] = A[pivot_index], A[r]

    return r

def findk(A,l,r):
    for i in main:

        if (l == r):
             return A[l]
        postion = partition(A, l, r)
        count = postion - l + 1
        if count == i :
             print( A[postion])
        elif ( count > i ) :
             print( findk(A, l, postion-1))
        else:
             print( findk(A, postion+1, r))
partition(a,0,len(a)-1)
g=(a,0,len(a)-1)
write("task5(b)_output.txt",g)