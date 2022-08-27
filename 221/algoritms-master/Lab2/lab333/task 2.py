def bfs(graph, start, end):
    visited = [0 for x in range(len(graph))]
    answer = []
    queue = []

    def bfs_engine(visited, graph, node, endpoint):
        visited[node-1 ] = 1
        queue.append(node)
        while queue:
            final_node = queue.pop(0)
            answer.append(final_node)
            if final_node == endpoint:
                break
            for neighbour in graph[final_node -1]:
                if visited[neighbour - 1] == 0:
                    visited[neighbour - 1] = 1
                    queue.append(neighbour)

    bfs_engine(visited, graph, int(start), int(end))
    return answer


f = open("input2.txt", 'r')
lines = f.readlines()
f.close()
n = int(lines[0])
adjlist = [[] for i in range(n)]
for i in range(2, len(lines)):
    first, second = lines[i].split()
    first, second = int(first), int(second)

    adjlist[first - 1].append(second)
print(adjlist)

answer = bfs(adjlist, 1, n)
final_output= " "
for i in answer:
    final_output+=f"{str(i)} "

g = open("output2.txt", 'w')
g.write( final_output)
g.close()


# # def bfs(graph, sP, eP):
# visited = [0 for x in range(len(graph))]
# answer = []
# queue = []
#
# def bfs_engine(visited, graph, node, endpoint):
#     global answer
#     visited = [0 for x in range(len(graph))]
#     # global visited[node - 1] = 1
#     queue.append(node)
#     while queue:
#         final_node = queue.pop(0)
#         answer.append(final_node)
#         if final_node == endpoint:
#             break
#         for neighbour in graph[final_node - 1]:
#             if visited[neighbour - 1] == 0:
#                 visited[neighbour - 1] = 1
#                 queue.append(neighbour)
#     return answer
#
# bfs_engine(visited, graph, int(sP), int(eP))
# # return answer


# file = open('input.txt', 'r')
# inp = (file.read()).split('\n')
#
# nodes = int(inp[0])
# edges = int(inp[1])
#
# # creating a graph
# graph = [set() for i in range(nodes + 1)]
#
# # adding edges to graph
# for line in inp[2:]:
#     x, y = map(int, line.split())
#     graph[x].add(y)
#
# # creating a visited list
# visited = [False for i in range(nodes + 1)]
# queue = []
#
# ans=[]


# f = open("input.txt", 'r')
# edges = f.readlines()
# f.close()
# vertices = int(edges[0])
# graph = [[] for i in range(vertices)]
# for i in range(2, len(edges)):
#     first, second = edges[i].split()
#     first, second = int(first), int(second)
#
#     graph[first - 1].append(second)
#
# # print(graph)
# visited = [False for i in range(vertices + 1)]
# queue = []
#
# ans = []
#
#
# # BFS function definition
# def BFS(visited, graph, node, endPoint):
#     visited[node] = 1
#     queue.append(node)
#     index = 0
#     global ans
#
#     while queue:
#         m = queue[index]
#         ans.append(m)
#         index += 1
#         if m == endPoint: break
#         for x in (graph[m]):
#             if visited[x] == 0:
#                 visited[x] = 1
#                 queue.append(x)
#
#
# BFS(visited, graph, 1, 12)
# ans_str = " ".join([str(x) for x in ans])
# g = open("output2.txt", 'w')
# g.write(ans_str)
# g.close()
