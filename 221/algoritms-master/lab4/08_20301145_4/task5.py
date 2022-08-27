from heapq import *
from collections import defaultdict


def dijkstra(graph, source):
    distance = defaultdict(lambda :-1)
    is_visited = defaultdict()
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

f = open("input5.txt", "r")
w = int(f.readline())
st=""
for _ in range(w):
    graph = defaultdict(list)
    vertices, edges = map(int, f.readline().strip().split())
    for i in range(edges):
        u, v, w = map(int, f.readline().strip().split())
        graph[u].append((v, w))
    source = int(f.readline())
    ans = dijkstra(graph, source)
    for i in range(1, vertices + 1):
        st+=str(ans[i])

o = open("output5.txt", "w")
for i in st:
    o.write(str(i) + " ")
