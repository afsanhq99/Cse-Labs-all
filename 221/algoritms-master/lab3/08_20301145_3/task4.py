

file=open("input4.txt","r")
lines=file.readlines()
v,e=lines[1].split()

adj=[[] for i in range(int(e))]
for i in range(2,4):
    f,s=lines[i].split()
    f,s=int(f),int(s)
    adj[f-1].append(s)
print(adj)
v1,e1=lines[4].split()
adj1=[[] for i in range(int(e1))]
for i in range(5,9):
    f,s=lines[i].split()
    f,s=int(f),int(s)
    adj1[f-1].append(s)
print(adj1)


visited= [0 for x in range(len(adj))]
answer = []
queue = []

def bfs(visited, graph, node, endpoint):
    visited[node-1 ] = 1
    queue.append(node)
    while queue:
        final_node = queue.pop(0)
        answer.append(final_node)
        if final_node == endpoint:
            break
        else:
            for neighbour in graph[final_node-1]:
                if visited[neighbour] == 0:
                    visited[neighbour] = 1
                    queue.append(neighbour)
    return answer
ans1= bfs(visited, adj, 1, v)

print(ans1)

visited2 = [0 for x in range(len(adj1))]
answer2 = []
queue2 = []

def bfs(visited2, graph, node, endpoint):
    visited2[node-1 ] = 1
    queue2.append(node)
    while queue:
        final_node = queue2.pop(0)
        answer2.append(final_node)
        if final_node == endpoint:
            break
        else:
            for neighbour in graph[final_node -1]:
                if visited2[neighbour - 1] == 0:
                    visited2[neighbour - 1] = 1
                    queue2.append(neighbour)
    return answer2
ans2= bfs(visited2, adj1, 1, v1)