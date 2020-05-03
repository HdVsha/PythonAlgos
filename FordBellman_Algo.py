class Graph:

    def __init__(self, vertices_num):
        self.V = vertices_num
        self.graph = []


    def addEdge(self, cur_v, neibr, wt):
        self.graph.append([cur_v, neibr, wt])


    def printArr(self, dist):

        for i in range(len(dist)):
            if abs(dist[i]) >= float("inf"):
                dist[i] = "UDF"
        print(*dist)


    def BellmanFord(self, dist):

        for _ in range(self.V - 1):

            # the analog of lector's "u, v, w"
            for cur_v, neibr, wt in self.graph:
                if (dist[cur_v] + wt < dist[neibr]) and (dist[cur_v] != float("inf")):
                    dist[neibr] = dist[cur_v] + wt

        for cur_v, neibr, wt in self.graph:
            if (dist[cur_v] + wt < dist[neibr]) and (dist[cur_v] != float("inf")):
                dist[neibr] = float("-inf")


        self.printArr(dist)

if __name__ == "__main__":
    N, M, start = map(int, input().split()) # N - number of vertexes, M - number of edges
    # initializing the graph
    g = Graph(N)

    for i in range(M):
        cur_vertex, neighbour, weight = map(int, input().split())
        g.addEdge(cur_vertex, neighbour, weight)


    dist = [float("Inf")] * N
    dist[start] = 0
    path = []


    g.BellmanFord(dist)
