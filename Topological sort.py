def dfs(vertex, G):
    used[vertex] = 1
    for neighbor in G[vertex]:
        if used[neighbor] == 0:
            dfs(neighbor,G)
        elif used[neighbor] == 1:
            stack.append(neighbor)
            print("NO")
            exit(0)
    used[vertex] = 2


def dfs_cycle(vertex, G,visited):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs_cycle(neighbor, G,visited)
    ans.append(vertex)



if __name__ == "__main__":
    n, m = map(int, input().split())
    G = [[] for i in range(n)]

    for j in range(m):
        start, finish = map(int, input().split())
        G[start].append(finish)
    used = [0] * n
    cycle = []
    stack = []
    for i in range(n):
        if used[i] == 0:
            dfs(i,G)

    if len(stack) == 0:
        visited = [False] *n
        ans = []
        for i in range(n):
            if not visited[i]:
                dfs_cycle(i,G,visited)
        ans[:] = ans[::-1]
        print(*ans)
