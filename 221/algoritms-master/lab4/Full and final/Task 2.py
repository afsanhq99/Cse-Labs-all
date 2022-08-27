import heapq
import math



def dijkstra(graph, source, V, E, path=dict()):
    dist = [math.inf for i in range(V + 1)]
    dist[source] = 0
    path[source] = [source]  # set source node path as itself
    queue = [[source, 0]]

    while queue:
        current_node, cost = heapq.heappop(queue)
        for adj in graph[current_node]:
            new_node, weight = adj
            if cost + weight < dist[new_node]:
                dist[new_node] = cost + weight

                path[new_node] = path[current_node] + [new_node]

                heapq.heappush(queue, [new_node, dist[new_node]])

    return path[V]


file = open("Task 1 input.txt", "r")
outFile = open("Task 2 output.txt", "w")

T = int(file.readline().strip())
final = []
for i in range(T):
    N, M = map(int, file.readline().strip().split())

    graph = [[] for i in range(N + 1)]
    for i in range(M):
        u, v, w = map(int, file.readline().strip().split())
        graph[u].append([v, w])
        graph[v].append([u, w])
    path = dijkstra(graph, 1, N, M)
    final.append(str(path))


str1 = ""
for i in final:
    print(i)
    outFile.write(i+"\n")
file.close()
outFile.close()