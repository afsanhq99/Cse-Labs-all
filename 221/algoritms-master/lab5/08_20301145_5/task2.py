
f=open("task2_input.txt", "r")
a=f.readlines()
start=[]
finish=[]
for i in a:
    x,y=i.strip().split(" ")
    start.append(x)
    finish.append(y)
n = len(finish)
i = 0
count =0
g = ""
for j in range(n):
    if start[j] >= finish[i]:
        count+=1
        i = j
g+=str(count)

o=open("task2_output.txt", "w")
o.write(g)




