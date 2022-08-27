"""
Problem 04: Matrix Multiplication
"""


def multiply_matrix(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def read_input():
    print("Reading Matrix A from input file...")
    input_a = open("input_A.txt", "r")

    print("Reading Matrix B from input file...")
    input_b = open("input_B.txt", "r")

    A = []
    B = []
    for row in input_a:
        cur_row = row.split(' ')
        for i in range(len(cur_row)):
            cur_row[i] = int(cur_row[i])
        A.append(cur_row)

    for row in input_b:
        cur_row = row.split(' ')
        for i in range(len(cur_row)):
            cur_row[i] = int(cur_row[i])
        B.append(cur_row)
    input_a.close()
    input_b.close()
    return A, B


def write_to_output(C):
    print("Writing result to output file...")
    output_file = open("output product.txt", "w")
    for row in C:
        row_str = ""
        for element in row:
            row_str += str(element) + " "
        row_str += "\n"
        output_file.write(row_str)

    output_file.close()



A, B = read_input()
print("Calculating the product....")
C = multiply_matrix(A, B)
write_to_output(C)
print("...done")