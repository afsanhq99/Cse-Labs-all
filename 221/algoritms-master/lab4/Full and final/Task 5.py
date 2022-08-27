from heapq import *
from collections import defaultdict


def dijkstra(graph, source):
    distance = defaultdict(lambda :-1)
    is_visited = defaultdict(int)
    distance[source] = 0
    heap = [(0, source)]
    while heap:
        curr_dist, node = heappop(heap)
        curr_dist = -curr_dist
        is_visited[node] = True
        for adjacent_node, weight in graph[node]:
                if (curr_dist == 0):
                    if distance[adjacent_node] < weight:
                        distance[adjacent_node] = weight
                        heappush(heap, (-weight, adjacent_node))
                elif distance[adjacent_node] < min(curr_dist, weight):
                    distance[adjacent_node] = min(curr_dist, weight)
                    heappush(heap, (min(curr_dist, weight), adjacent_node))
    return distance

f = open("Task 5 input.txt", "r")
w = int(f.readline())
st=""
for _ in range(w):
    graph = defaultdict(list)
    n, m = f.readline().strip().split()
    n, m = int(n), int(m)
    for i in range(m):
        u, v, w = f.readline().strip().split()
        u, v, w = int(u), int(v), int(w)
        graph[u].append((v, w))
    source = int(f.readline())
    ans = dijkstra(graph, source)
    for i in range(1, n + 1):
        st+=str(ans[i])

o = open("Task 5 output.txt", "w")
for i in st:
    o.write(str(i) + " ")
