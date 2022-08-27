# """
#     Python code to find the places one needs to visit
#     to get to the target location
# """
# # importing defaultdict for creating graph
# from collections import defaultdict
#
#
# # Graph class to represent a graph using adjacency list representation
# class Graph:
#     h = []
#     # Constructor of Graph class
#     def __init__(self):
#         # default dictionary to store graph
#         self.graph = defaultdict(list)
#
#     # Function to add an edge
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     # DFSUtil method that is recursively called by main DFS method
#     def DFSHelper(self, v, visited, solution, t):
#         # Adding the current node to visited set
#         visited.add(v)
#         # Adding the current node to the solution list
#         solution.append(v)
#         # Recursively called DFSHelper method for all the neighbours of current vertex
#         for neighbour in self.graph[v]:
#             if neighbour not in visited and t not in visited:
#                 self.DFSHelper(neighbour, visited, solution, t)
#
#     # Main DFS method that will find the path from starting to target using DFS
#     def DFS(self, s, t):
#         # Visited set to store all vertices that are visited
#         visited = set()
#         # Solution list to store the path
#         solution = []
#         # call the recursive helper function to print path using DFS algorithm
#         for vertex in list(self.graph):
#             if vertex not in visited and t not in visited:
#                 self.DFSHelper(vertex, visited, solution, t)
#         # calling printSolution to print the path
#         self.printSolution(solution)
#
#     # PrintSolution method to print the final path solution
#     def printSolution(self, solution):
#         global h
#
#         for v in solution:
#             h.append(v)
#
#
#
# # main method of code
# # creates a graph reading input.txt
# def main():
#     g = Graph()
#     inputFile = open("input.txt", "r")
#     vertices = int(inputFile.readline())
#     edges = int(inputFile.readline())
#     line = inputFile.readline()
#     startingVertex = -1
#     targetVertex = -1
#     while line != "":
#         if startingVertex == -1:
#             startingVertex = int(line.split()[0].strip())
#         g.addEdge(int(line.split()[0].strip()), int(line.split()[1].strip()))
#         targetVertex = int(line.split()[1].strip())
#         line = inputFile.readline()
#     inputFile.close()
#     g.DFS(startingVertex, targetVertex)
# h=[]
# main()
# print(h)
# f=open("output3.txt","w")
# ans_str = " ".join([str(x) for x in h])
#
# f.write(str(ans_str))


#
output = []
def dfs(visited, graph, node, destination):
    global output
    if destination in visited:
        return
    if node not in visited:
        output.append(node)
    visited.add(node)
    if node not in graph:
        return
    for neighbour in graph[node]:

        dfs(visited, graph, neighbour, destination)
def path():
    with open("input.txt") as file:
        vertices = int(file.readline())
        edges = int(file.readline())
        graph = {}
        for i in range(edges):
            source, destination = map(int, file.readline().split())
            if source in graph:
                graph[source].append(destination)
            else:
                graph[source] = [destination]
        visited = set()
        dfs(visited, graph, 1, vertices)


a=path()
final_output= " "
for i in output:
    final_output+=f"{str(i)} "
f=open("output3.txt","w")

f.write(final_output)
f.close()


