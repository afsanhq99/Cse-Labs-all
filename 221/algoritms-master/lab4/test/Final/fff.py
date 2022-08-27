from heapq import *
from collections import defaultdict
from queue import PriorityQueue
import math


def dijkstra(graph, source):
    queue = PriorityQueue()
    is_visited = [False] * len(graph)
    distance = [math.inf] * len(graph)
    distance[source] = 0
    queue.put((distance[source], source))
    while queue:
        curr_dist, node = queue.get()[0],queue.get()[1]
        curr_dist = -curr_dist
        is_visited[node] = True
        for adjacent_node, weight in graph[node]:
                if (curr_dist == 0):
                    if distance[adjacent_node] < weight:
                        distance[adjacent_node] = weight
                        queue.put(queue, (-weight, adjacent_node))
                elif distance[adjacent_node] < min(curr_dist, weight):
                    distance[adjacent_node] = min(curr_dist, weight)
                    queue.put(queue, (min(curr_dist, weight), adjacent_node))
    return distance

f = open("Task 5 input.txt", "r")
t = int(f.readline())
st=""
for _ in range(t):
    graph = defaultdict(list)
    n, m = f.readline().strip().split()
    n, m = int(n), int(m)
    for i in range(m):
        s, d, t = f.readline().strip().split()
        s, d, t = int(s), int(d), int(t)
        graph[s].append((d, t))
    source = int(f.readline())
    ans = dijkstra(graph, source)
    for i in range(1, n + 1):
        st+=str(ans[i])

o = open("Task 5 output.txt", "w")
for i in st:
    o.write(str(i) + " ")
