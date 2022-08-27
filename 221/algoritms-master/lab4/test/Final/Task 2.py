# # from heapq import heapify, heappop, heappush
# # from collections import defaultdict
# #
# #
# # def dijkstra(graph, source):
# #     n = len(graph)
# #
# #     # initalse a distance array of size equal to number of nodes
# #     distance = defaultdict(lambda: float('inf'))
# #
# #     visited = defaultdict(int)
# #     # initalise dist from source to be 0
# #     distance[source] = 0
# #     parent = defaultdict(str)
# #
# #     # now we will creat a heap and push the starting vertex and it's distance
# #     heap = [(0, source)]
# #     heapify(heap)
# #     # continue the loop till all the vertices are traversed
# #     while heap:
# #
# #         # pop out elements from the heap
# #         dist, node = heappop(heap)
# #         # if we reach to the destination
# #
# #         # mark it visited
# #         visited[node] = 1
# #         # now traverse all the neighbor of the node a
# #         # put them into the heap
# #         for adj, weight in graph[node]:
# #             # check if adj exist and is unvisited
# #             if visited[adj] == False:
# #                 # check if the currect distance from the source
# #                 # more than caculated distance
# #                 if distance[adj] > dist + weight:
# #                     # update the distance and push it into the heap
# #                     distance[adj] = dist + weight
# #                     heappush(heap, (dist + weight, adj))
# #                     parent[adj] = node
# #     # now after traversing all the nodes
# #     # which are included in the path reverse from destination to source
# #     ans = []
# #     node = n
# #
# #     while node != 1:
# #         ans.append(node)
# #         node = parent[node]
# #     ans.append(1)
# #     # return the list in reverse order
# #     return ans[::-1]
# #
# #
# # # driver code
# # f = open("Task 2 input.txt", "r")
# # t = int(f.readline())
# # g = ""
# # h = []
# # for _ in range(t):
# #     # construiting the graph first
# #     graph = defaultdict(list)
# #
# #     # propmt the user to enter the vertices and then the edges
# #     N, M = f.readline().split()
# #     N = int(N)
# #     M = int(M)
# #     for i in range(M):
# #         # enter source , destination and weight of the edge
# #         s, d, t = map(int, f.readline().split())
# #         graph[s].append((d, t))
# #         graph[d].append((s, t))
# #     print(graph)
# #     if N != 1:
# #         ans = dijkstra(graph, 1)
# #         h.append(ans)
# #         for num in ans :
# #             g+=str(num)
# #     else:
# #         h.append([1])
# #
# # print(h)
# # hs=""
# # f=open("Task 2 output.txt","w")
# # for i in h:
# #         hs+=str(i)+" \n"
# # for i in hs:
# #     f.write(i)
# #
# from heapq import heapify, heappop, heappush
# from collections import defaultdict
# from queue import *
# import math
#
# def dijkstra(graph, source):
#     queue = PriorityQueue()
#     visited = [False] * len(adj_list)
#     distance = [math.inf] * len(adj_list)
#     distance[source] = 0
#     queue.put((distance[source], source))
#
#     # continue the loop till all the vertices are traversed
#     while queue:
#
#         # pop out elements from the heap
#         dist = queue.get()[0]
#         node=queue.get()[1]
#         # if we reach to the destination
#
#         # mark it visited
#         visited[node] = 1
#         # now traverse all the neighbor of the node a
#         # put them into the heap
#         for adj, weight in graph[node]:
#             # check if adj exist and is unvisited
#             if visited[adj] == False:
#                 # check if the currect distance from the source
#                 # more than caculated distance
#                 if distance[adj] > dist + weight:
#                     # update the distance and push it into the heap
#                     distance[adj] = dist + weight
#                     queue.put((distance[adj[0]]),weight)
#                     # heappush(heap, (dist + weight, adj))
#                     parent[adj] = node
#     # now after traversing all the nodes
#     # which are included in the path reverse from destination to source
#     ans = []
#     node = n
#
#     while node != 1:
#         ans.append(node)
#         node = parent[node]
#     ans.append(1)
#     # return the list in reverse order
#     return ans[::-1]
#
#
# # driver code
# f = open("Task 2 input.txt", "r")
# t = int(f.readline())
# g = ""
# h = []
# for _ in range(t):
#     # construiting the graph first
#     graph = defaultdict(list)
#
#     # propmt the user to enter the vertices and then the edges
#     N, M = f.readline().split()
#     N = int(N)
#     M = int(M)
#     for i in range(M):
#         # enter source , destination and weight of the edge
#         s, d, t = map(int, f.readline().split())
#         graph[s].append((d, t))
#         graph[d].append((s, t))
#     print(graph)
#     if N != 1:
#         ans = dijkstra(graph, 1)
#         h.append(ans)
#         for num in ans :
#             g+=str(num)
#     else:
#         h.append([1])
#
# print(h)
# hs=""
# f=open("Task 2 output.txt","w")
# for i in h:
#         hs+=str(i)+" \n"
# for i in hs:
#     f.write(i)
#
import heapq # import priority queue
from math import inf as  infinity

def dijkstra(graph,source,V,E,path = dict()):
        dist = [infinity for i in range(V + 1)]
        dist[source] = 0
        path[source] = [source] # set source node path as itself
        queue =  [[source,0]]

        while queue:
                current_node, cost = heapq.heappop(queue)
                for adj in graph[current_node]:
                        v , wt = adj
                        if cost + wt < dist[v]:
                                dist[v] = cost + wt

                                path[v] = path[current_node] + [v]

                                heapq.heappush(queue,[v, dist[v]])

        return path[V]



file = open("Task 1 input.txt","r")
outFile = open("Task 2 output.txt","w")



T = int(file.readline().strip())
final=[]
for i in range(T):
        N,M = map(int,file.readline().strip().split())

        graph =[ [] for i in range(N + 1)]
        for i in range(M):
                u,v,w = map(int,file.readline().strip().split())
                graph[u].append([v,w])
                graph[v].append([u,w])
        path = dijkstra(graph,1,N,M)
        final.append(str(path))

print(final)
str1 = ""
for i in final:
        print(i)
        outFile.write(i)
file.close()
outFile.close()
