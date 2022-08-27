from file_io import read,write 


def merge(a, p, q, r, b):
    left = p
    right = q + 1

    while p <= r:

        if  (right > r or a[left] <= a[right]):
            b[p] = a[left]
            left += 1
        else:
            b[p] = a[right]
            right += 1

        p += 1
    for i in range(len(a)):
        a[i] = b[i]


def merge_sort(a, p, r, b=[]):
    if p >= r:
        return
    if not len(b):
        b=[]
        for i in range(len(a)):
            b.append(a[i])
    q = (p + r) // 2
    merge_sort(a, p, q, b)
    merge_sort(a, q + 1, r, b)
    merge(a, p, q, r, b)
    return b


a = read("task4_input1.txt")
a = merge_sort(a, 0, len(a) - 1)
write("task4_output1.txt", a)

b = read("task4_input2.txt")
b = merge_sort(b, 0, len(b) - 1)
write("task4_output2.txt", b)