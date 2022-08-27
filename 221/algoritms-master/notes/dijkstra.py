from queue import PriorityQueue
import math


def Dijkstra(adj_list, source):
    queue = PriorityQueue()
    isVisited = [False] * len(adj_list)
    distance = [math.inf] * len(adj_list)
    distance[source] = 0
    queue.put((distance[source], source))
    while not queue.empty():
        present_node = queue.get()[1]
        if isVisited[present_node]:
            continue
        else:
            isVisited[present_node] = True
            for nodes in adj_list[present_node]: #node[0]=vertex name,  node[1]=weight between present node and node
                alt_weight = distance[present_node] + nodes[1]
                if alt_weight < distance[nodes[0]]:
                    distance[nodes[0]] = alt_weight
                    queue.put((distance[nodes[0]], nodes[0]))

    return distance[len(adj_list) - 1]
