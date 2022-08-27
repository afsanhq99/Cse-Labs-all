import heapq
import math


def dijkstra(graph, source,V,E):
    path = dict()
    dist = [math.inf for i in range(V + 1)]
    dist[source] = 0
    path[source] = [source]
    queue = [(source, 0)]

    while queue:
        current_node, cost = heapq.heappop(queue)
        for adj in graph[current_node]:
            new_node, weight = adj
            if cost + weight < dist[new_node]:
                dist[new_node] = cost + weight

                path[new_node] = path[current_node] + [new_node]

                heapq.heappush(queue, (new_node, dist[new_node]))

    return path[V]


file = open("input2.txt", "r")

T = int(file.readline().strip())
final = []
for i in range(T):
    vertices, edges = map(int, file.readline().strip().split())
    graph = [[] for i in range(vertices + 1)]
    for i in range(edges):
        u, v, w = map(int, file.readline().strip().split())
        graph[u].append([v, w])
        graph[v].append([u, w])
    print(graph)
    path = dijkstra(graph, 1, vertices, edges)
    final.append(str(path))
outFile = open("output2.txt", "w")

str1 = ""
for i in final:
    outFile.write(i + "\n")
file.close()
outFile.close()
