# with open("input.txt") as f:
#     lines = f.readlines()
#
#     f.close()
#     vertices = int(lines[0])
#     adjacent_list = [[] for i in range(vertices)]
#     for i in range(2, len(lines)):
#         first, second = lines[i].split()
#         first, second = int(first), int(second)
#
#         adjacent_list[first - 1].append(second)
#
#     print(adjacent_list)
#
#
# with open("input.txt") as file:
#     vertices = int(file.readline())
#     edges = int(file.readline())
#     graph = {}
#     for i in range(edges):
#         source, destination = map(int, file.readline().split())
#         if source in graph:
#             graph[source].append(destination)
#         else:
#             graph[source] = [destination]
#     visited = set()
#     print(graph)
#
def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)]
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1
        visited[src] = True
        dist[src] = 0; queue.append(src) #--------------------------------------put next code(while loop) from this indentation
        while (len(queue) != 0):
            u = queue[0]; queue.pop(0)
            for i in range(len(adj[u])):
                if (visited[adj[u][i]] == False):
                    visited[adj[u][i]] = True
                    dist[adj[u][i]] = dist[u] + 1
                    pred[adj[u][i]] = u
                    queue.append(adj[u][i])
                    if (adj[u][i] == dest):
                        return True
                    return False
def printShortestDistance(adj, s, dest, v):
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
        path = []
        crawl = dest
        crawl = dest
        path.append(crawl) #----------------------------put next code(while loop of pred[craw] one) from this indentation
        while (pred[crawl] != -1):
            path.append(pred[crawl])
            crawl = pred[crawl]
            print("Shortest path length is : " + str(dist[dest]))

if __name__=='__main__':
     T=int(input())
     while(T>0):
         ver=int(input())
         edg=int(input())
         adj = [[] for i in range(ver)]
         for j in range(edg):
             a=int(input())
             b=int(input())
             add_edge(adj, a-1, b-1)
             printShortestDistance(adj, 0, ver-1, ver)