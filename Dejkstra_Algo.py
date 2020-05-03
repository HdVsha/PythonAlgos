from collections import deque
from collections import OrderedDict


def show_shortest_path(graph, start, finish, dist, weights):
    tmp_queue = deque()
    path = []
    tmp_queue.append(finish)
    path.append(finish)
    
    while tmp_queue:
        cur_parent = tmp_queue.popleft()
        for parent in graph[cur_parent]:
            if weights[cur_parent, parent] + dist[parent] == dist[cur_parent]:
                path.append(parent)
                tmp_queue.append(parent)

    return path[::-1]


def initialize_graph(graph, weights):
    for i in range(M):
        v1, v2, weight = input().split()
        v1, v2 = int(v1), int(v2)
        weight = float(weight)
        graph[v1].add(v2)
        graph[v2].add(v1)
        weights[v1, v2] = weight
        weights[v2, v1] = weight


def Dejkstra(queue, dist):
    while queue:
        cur_vertex = queue.popleft()
        for neighbour in graph[cur_vertex]:
            if weights[cur_vertex, neighbour] + dist[cur_vertex] < dist[neighbour]:
                dist[neighbour] = weights[cur_vertex, neighbour] + dist[cur_vertex]
                queue.append(neighbour)



if __name__ == "__main__":
    N, M, start, finish = map(int, input().split())   # N - number of vertexes, M - number of edges

    graph = {i: set() for i in range(N)}
    weights = OrderedDict()
    dist = [float('inf')] * N
    queue = deque()
    parents = [None] * N

    queue.append(start)
    dist[start] = 0

    initialize_graph(graph, weights)

    Dejkstra(queue, dist)

    shortest_path = show_shortest_path(graph, start, finish, dist, weights)

    print(*shortest_path)
