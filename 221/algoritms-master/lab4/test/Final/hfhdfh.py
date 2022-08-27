

from queue import PriorityQueue


import math

# INF=1
# we're using a well known technique of converting min queue to max queue that is we use negative of numbers so it works as max priority queue

def dijkstra(graph, source, N):
    # set distance INF for all
    # distance = [math.inf for i in range(N)]
    distance=[math.inf]*len(graph)

    # create priorityQueue
    queue = PriorityQueue()
    # initializing source to INF as source can send INF to any node=
    distance[source] = math.inf
    queue.put([distance[source], 0])
    # visit all nodes with distance as queue priority
    while not queue.empty():
        temp, current = queue.get()
        for i in range(N):
            # if not INF means it's neighbour of current
            if graph[current][i] != math.inf:
                newDistance = min(distance[current], graph[current][i])
                # if new distance is greater than new, update distance
                if newDistance > distance[i]:
                    queue.put([newDistance, i])
                    distance[i] = newDistance
    distance[source] = 0
    # print(distance)

    outputString = ""
    for i in range(N):
        outputString += str(distance[i])+" "
    return outputString


# reading input file
file = open("Task 5 input.txt","r")
# opening output file
outputFile = open("Task 5 output.txt", "w")
# read number of testcase
numbersOfTestCases = int(file.readline())
outputString = ""
for _ in range(numbersOfTestCases):
    # get input
    device, links = map(int, file.readline().split())
    graph = [[math.inf for i in range(device)] for j in range(device)]

    # update adjaceny matrix with weights
    for i in range(links):
        src, dest, weight = map(int, file.readline().split())
        src -= 1
        dest -= 1
        graph[src][dest] = weight
        # print(graph)
    source = int(file.readline())
    # print(source)
    source -= 1
    # print(graph)
    # call dijsktra and output the values
    # print(dijkstra(graph, source, N))
    outputFile.write(str(dijkstra(graph, source, device)) + "\n")
# file.close()
# outputFile.close()


# from queue import PriorityQueue
#
# INF = 10 ** 9
#
#
# # we're using a well known technique of converting min queue to max queue that is we use negative of numbers so it works as max priority queue
#
# def dijkstra(graph, source, N):
#     # set distance INF for all
#     distance = [-1 for i in range(N)]
#     # create priorityQueue
#     queue = PriorityQueue()
#     # initializing source to INF as source can send INF to any node=
#     distance[source] = INF
#     queue.put([distance[source], 0])
#     # visit all nodes with distance as queue priority
#     while not queue.empty():
#         temp, current = queue.get()
#         for i in range(N):
#             # if not INF means it's neighbour of current
#             if graph[current][i] != INF:
#                 newDistance = min(distance[current], graph[current][i])
#                 # if new distance is greater than new, update distance
#                 if newDistance > distance[i]:
#                     queue.put([-newDistance, i])
#                     distance[i] = newDistance
#     distance[source] = 0
#     return distance
#
#     # outputString = ""
#     # for i in range(N):
#     #     outputString += str(distance[i])+" "
#     # return outputString
#
#
# # reading input file
# file = open("input5.txt","r")
# # opening output file
# outputFile = open("Task 5 output.txt", "w")
# # read number of testcase
# numbersOfTestCases = int(file.readline())
# outputString = ""
#
# for _ in range(numbersOfTestCases):
#     # get input
#     N, M = map(int, file.readline().split())
#     graph = [[INF for i in range(N)] for j in range(N)]
#     # update adjaceny matrix with weights
#     for i in range(M):
#         u, v, w = map(int, file.readline().split())
#         u -= 1
#         v -= 1
#         graph[u][v] = w
#     source = int(file.readline())
#     source -= 1
#     j=dijkstra(graph,source,N)
#     print(j)
#     for i in range(N):
#         outputString += str(j[i])+"\n "
#
#     # call dijsktra and output the values
#     # print(dijkstra(graph, source, N))
#
#     # outputFile.write(str(dijkstra(graph, source, N)) + "\n")
# print(outputString)
# # file.close()
# # outputFile.close()