
import math
f=open("task4_input.txt", "r")
lines=f.readlines()
count=0
g=""
for i in lines:
    a,b=i.strip().split(" ")
    a,b=int(a),int(b)
    if a==0 and b==0:
        break
   
    for i in range(a,b+1):
        f=str(math.sqrt(i))
        a=f.split('.')
        if a[1]=="0":
            count+=1
        elif a[0]=="0":
            count=0

    g+=str(count)+"\n"


o = open("task4_output.txt", "w")
o.write(g)