import sys

def dfs(idx):
    global count
    visited[idx] = True

    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            count += 1
            dfs(next)

count = 0
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(count)