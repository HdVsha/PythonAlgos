"""
In the previous task I forgot to delete the unnecessary code. Sorry.
"""
class Graph_of_dist:

    def __init__(self, vertices_num): #initializing the graph of distances
        self.V = vertices_num
        self.graph_dist = [[float("inf")] * self.V for _ in range(self.V)]
        for i in range(self.V):
            self.graph_dist[i][i] = 0



    def addEdge(self, cur_v, neibr, wt):
        self.graph_dist[cur_v][neibr] = wt
        self.graph_dist[neibr][cur_v] = wt

    def printArr(self):
        finish_sum = float("inf")
        ind_of_cap = float("inf")

        for v1 in range(self.V):
            sum = 0
            for v2 in g.graph_dist[v1]:
                sum += v2
            if sum < finish_sum:
                ind_of_cap = v1
                finish_sum = sum

        print(ind_of_cap)


    def FloydWarshall(self):

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if g.graph_dist[i][j] > g.graph_dist[i][k] + g.graph_dist[k][j]:
                        g.graph_dist[i][j] = g.graph_dist[i][k] + g.graph_dist[k][j]

        self.printArr()

if __name__ == "__main__":
    N, M = map(int, input().split()) # N - number of vertexes, M - number of edges
    # initializing the graph
    g = Graph_of_dist(N)

    for i in range(M):
        cur_vertex, neighbour, weight = map(int, input().split())
        g.addEdge(cur_vertex, neighbour, weight)

    g.FloydWarshall()

