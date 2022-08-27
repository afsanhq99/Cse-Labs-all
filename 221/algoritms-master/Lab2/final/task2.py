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


def selection_sort(a):
    for i in range(len(a) - 1):
        min_val = a[i]
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        if min_val < a[i]:
            a[i], a[min_index] = a[min_index], a[i]



a = read("task2_input1.txt")
selection_sort(a)
write("task2_output1.txt", a)

b = read("task2_input2.txt")
selection_sort(b)
write("task2_output2.txt", b)