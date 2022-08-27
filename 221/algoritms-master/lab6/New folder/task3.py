def LCS(a, b, c):
    arr = [[[0 for k in range(len(c) + 1)]
            for j in range(len(b) + 1)]
           for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if i == 0 or j == 0 or k==0:
                    arr[i][j][k] = 0
                elif x == y and y == z:
                    arr[i + 1][j + 1][k + 1] = arr[i][j][k] + 1
                else:
                    arr[i + 1][j + 1][k + 1] = max(arr[i + 1][j + 1][k], arr[i][j + 1][k + 1], arr[i + 1][j][k + 1])
    return arr[-1][-1][-1]

f=open("task3_input2.txt","r")
b=f.readlines()

print(b[0])
b1=LCS(str(b[0]),str(b[1]),str(b[2]))
g1=""
g1+=str(b1)
f1=open("task3_output2.txt","w")
f1.write(g1)




