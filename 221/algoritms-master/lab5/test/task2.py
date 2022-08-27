
f=open("task2_input.txt", "r")
a=f.readlines()
first=[]
second=[]
for i in a:
    x,y=i.strip().split(" ")
    first.append(x)
    second.append(y)
n = len(second)
i = 0
count =0
g = ""
for j in range(n):
    if first[j] >= second[i]:
        count+=1
        i = j
g+=str(count)

o=open("task2_output.txt", "w")
o.write(g)




