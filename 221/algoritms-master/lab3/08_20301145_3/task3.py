
output = []
visited = set()
def dfs(visited, graph, node, destination):
    global output
    if destination in visited:
        return
    if node not in visited:
        output.append(node)
        visited.add(node)
    if node not in graph:
        return
    for neighbour in graph[node]:

        dfs(visited, graph, neighbour, destination)
def path():
    file=open("input.txt","r")
    vertices = int(file.readline())
    edges = int(file.readline())
    graph = {}
    for i in range(edges):
        source, destination = map(int, file.readline().split())
       
        if source in graph:
            graph[source].append(destination)
        else:
            graph[source] = [destination]

    dfs(visited, graph, 1, vertices)
    print(graph)
a=path()

final_output= " "
for i in output:
    final_output+=f"{str(i)} "
f=open("output3.txt","w")

f.write(final_output)
f.close()


