from heapq import heapify, heappop, heappush
from collections import defaultdict
import math


# function to find the shortest path
def dijkstra(graph, source):
    n = len(graph)
    # initalse a distance array of size equal to number of nodes
    distance = [math.inf] * len(graph)
    distance[source] = 0

    visited = False*len(graph)


    # now we will creat a heap and push the starting vertex and it's distance
    heap = [(0, source)]
    heapify(heap)
    # continue the loop till all the vertices are traversed
    while heap:

        # pop out elements from the heap
        dist, node = heappop(heap)
        dist = -dist

        # mark it visited
        visited[node] = True
        # now traverse all the neighbor of the node a
        # put them into the heap
        for nbr, t in graph[node]:
            # check if nbr exist and is unvisited
            if visited[nbr] == False:

                if (dist == 0):
                    if distance[nbr] < t:
                        # update the distance and push it into the heap
                        distance[nbr] = t

                        heappush(heap, (-t, nbr))
                # check if the currect distance from the source
                # more than caculated distance
                elif distance[nbr] < min(dist, t):
                    # update the distance and push it into the heap
                    distance[nbr] = min(dist, t)
                    heappush(heap, (-min(dist, t), nbr))

    return distance


# driver code
f = open("Task 5 input.txt", "r")
t = int(f.readline())
h = []
st=""
for _ in range(t):
    # construiting the graph first


    # propmt the user to enter the vertices and then the edges
    n, m = f.readline().strip().split()
    n, m = int(n), int(m)
    graph = [[] for x in range(m + 1)]
    for i in range(m):
        # enter source , destination and weight of the edge
        s, d, t = f.readline().strip().split()
        s, d, t = int(s), int(d), int(t)
        graph[s].append((d, t))

    source = int(f.readline())
    ans = dijkstra(graph, source)
    for i in range(1, n + 1):

        st+=str(ans[i])


o=open("Task 5 output.txt","w")
for i in st:
    o.write(str(i)+" ")
