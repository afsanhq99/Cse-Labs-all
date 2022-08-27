f = open("input.txt", 'r')
lines = f.readlines()


f.close()
vertices = int(lines[0])
adjacent_list = [[] for i in range(vertices)]
for i in range(2, len(lines)):
    first, second = lines[i].split()
    first,second=int(first),int(second)


    adjacent_list[first-1].append(second)

print(adjacent_list)

