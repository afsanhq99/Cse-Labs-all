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


def merge_sort(a, p, r):
    if p >= r:
        return

    b=[]

    for i in range(len(a)):
        b.append(a[i])
    q = (p + r) // 2
    merge_sort(a, p, q)
    merge_sort(a, q + 1, r)
    merge(a, p, q, r,b)
    return b


a = read("task4_input1.txt")
a = merge_sort(a, 0, len(a) - 1)
write("task4_output1.txt", a)

b = read("task4_input2.txt")
b = merge_sort(b, 0, len(b) - 1)
write("task4_output2.txt", b)