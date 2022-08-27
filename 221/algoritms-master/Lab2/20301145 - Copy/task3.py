from file_io import read,write 


def insertion_sort(students, marks):
    for i in range(1, len(marks)):
        j = i - 1
        cur_a = students[i]
        cur_b = marks[i]
        while j >= 0 and cur_b > marks[j]:
            students[j + 1] = students[j]
            students[j] = cur_a
            marks[j + 1] = marks[j]
            marks[j] = cur_b
            j -= 1


students, marks = read("task3_input1.txt")
insertion_sort(students, marks)
write("task3_output1.txt", students)

c, d = read("task3_input2.txt")
insertion_sort(c, d)
write("task3_output2.txt", c)