
# f = open("input.txt", 'r')
# lines = f.readlines()
# f.close()
# vertex = int(lines[0])
# adjlist = [[] for i in range(vertex)]
# for i in range(2, len(lines)):
#     first, second = lines[i].split()
#     first, second = int(first), int(second)

#     adjlist[first - 1].append(second)


# visited = [0 for x in range(len(adjlist))]
# answer = []
# queue = []

# def bfs(visited, graph, node, endpoint):
#     visited[node-1 ] = 1
#     queue.append(node)
#     while queue:
#         final_node = queue.pop(0)
#         answer.append(final_node)
#         if final_node == endpoint:
#             break
#         else:
#             for adjecent in graph[final_node-1]:
#                 if visited[adjecent - 1] == 0:
#                     visited[adjecent - 1] = 1
#                     queue.append(adjecent)
#     return answer


# ans= bfs(visited, adjlist, 1, vertex)
# final_output= " "
# for i in ans:
#     final_output+=f"{str(i)} "

# g = open("output2.txt", 'w')
# g.write( final_output)
# g.close()

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

visited = [0 for x in range(len(graph))]
print (visited)
print(graph)
answer = []
queue = []

def bfs(visited, graph, node, endpoint):
    visited[node ] = 1
    queue.append(node)
    while queue:
        final_node = queue.pop(0)
        answer.append(final_node)
        if final_node == endpoint:
            break
        else:
            for adjecent in graph[final_node]:
                if visited[adjecent-1 ] == 0:
                    visited[adjecent-1 ] = 1
                    queue.append(adjecent)
    return answer


ans= bfs(visited, graph, 1, vertices)
final_output= " "
for i in ans:
    final_output+=f"{str(i)} "

g = open("output2.txt", 'w')
g.write( final_output)
g.close()