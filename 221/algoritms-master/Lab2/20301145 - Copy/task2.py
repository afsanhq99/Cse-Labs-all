from file_io import read,write 


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