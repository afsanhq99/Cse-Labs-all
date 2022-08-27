
def lcs(x, y, r, c):
        arr = [[0 for x in range(c + 1)] for x in range(r + 1)]

        for i in range(r + 1):
                for j in range(c + 1):
                        if i == 0 or j == 0:
                                arr[i][j] = 0
                        elif x[i - 1] == y[j - 1]:
                                arr[i][j] = arr[i-1][j-1] + 1
                        else:
                                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

        index = arr[r][c]
        lcs = [""] * (index+1)
        lcs[index] = ""

        i = r
        j = c
        while i > 0 and j > 0:
                if x[i - 1] == y[j - 1]:
                        lcs[index-1] = x[i - 1]
                        i-=1
                        j-=1
                        index-=1
                elif arr[i-1][j] > arr[i][j-1]:
                        i-=1
                else:
                        j-=1
        return "".join(lcs)


dict =  {
  "Y": "Yasnaya",
  "R": "Rozhok",
  "S": "School",
  "P": "Pochinki",
  "F": "Farm",
  "M": "Mylta",
  "H": "Shelter",
  "I": "Prison"
}
f=open("task2_input.txt","r")
n=int(f.readline())
X=f.readline()
Y=f.readline()


var= lcs(X, Y, n, n)

g=""
result = (len(var)*100)/8
f1=open("task2_output.txt","w")
for i in var:
    g+=dict[i]+" "

f1.write(g+"\n")
print("")
f1.write("Correctness of result :")
result1=str(result)
f1.write(result1+"%")





