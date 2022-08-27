
file = open("task3_input.txt", "r")
f = file.readlines()
tasks=[]
for i in f[1].split():
    tasks.append(int(i))
tasks.sort()
calls = f[2].strip()
count = 0
jack = []
ans = []
for j in calls:
    if j == "J":
        ans.append(tasks[count])
        jack.append(tasks[count])
        count += 1
    elif j == "j":
        ans.append(jack.pop())

g=""
for i in ans:
    g+=str(i)

o=open("task3_output.txt", "w")
for i in g:
    o.write(i)


