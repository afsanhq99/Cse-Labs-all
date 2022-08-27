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
def insertion_sort(students, marks):
    for i in range(1, len(marks)):
        j = i - 1
        students0 = students[i]
        marks0 = marks[i]
        while j >= 0 and marks0 > marks[j]:
            students[j + 1] = students[j]
            students[j] = students0
            marks[j + 1] = marks[j]
            marks[j] = marks0
            j -= 1


students, marks = read("task3_input1.txt")
insertion_sort(students, marks)
write("task3_output1.txt", students)

c, d = read("task3_input2.txt")
insertion_sort(c, d)
write("task3_output2.txt", c)