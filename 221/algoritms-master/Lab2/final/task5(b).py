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
# print(read("task5(b)_input.txt"))
main=a
# print(main)
k=read("task5(b)_input.txt")


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

def findk(main, l, r):

        for i in range(len(k)-1):
            if (l == r):
                 return main[l]
            postion = partition(main, l, r)
            presentindex = postion - l + 1
            if presentindex == i :
                 print(main[postion])
            elif ( presentindex > i ) :
                 print(findk(main, l, postion - 1))
            else:
                 print(findk(main, postion + 1, r))
partition(a,0,len(a)-1)
g=(a,0,len(a)-1)
gj=findk(main,0,len(main)-1)
write("task5(b)_output.txt",gj)
def findK(lst: list, idx: int) -> int:
    low = 0             # set low to 0
    high = len(lst)-1   # set high to last index of lst
    while low <= high:
        # getting the partition index
        partition_idx = partition(lst, low, high)
        if partition_idx == idx-1:
            # if partition idx is idx -1
            # here idx is considered as 1 index based
            # and list indexing is 0 index based
            # return the value
            return lst[partition_idx]
        elif partition_idx < idx-1:
            # if partition idx is less than the desired idx
            # then set low to partition_idx +1
            low = partition_idx + 1
        else:
            # else the partition idx is higher than desired idx
            # so set high to partition idx - 1
            high = partition_idx - 1


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 9, 7, 10]
    print(f'findK for K = 5: {findK(arr, 5)}')
    print(f'findK for K = 7: {findK(arr, 7)}')
    print(f'findK for K = 2: {findK(arr, 2)}')