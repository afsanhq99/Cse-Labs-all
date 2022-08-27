f = open("task1_input.txt", "r")
n = int(f.readline())
lst = []
for i in range(n):
    a = list(map(int, f.readline().split()))
    lst.append(a)
lst = sorted(lst, key=lambda x: x[1])
final = [lst[0]]
count = 1
second_elem = lst[0][1]
for j in range(len(lst) - 1):
    if (second_elem <= lst[j + 1][0]):
        final.append(lst[j + 1])
        second_elem = lst[j + 1][1]
        count += 1
o = open("task1_output.txt", "w")
g = ""
for j in final:
    g += str(j) + "\n"
for i in g:
    o.write(i)
