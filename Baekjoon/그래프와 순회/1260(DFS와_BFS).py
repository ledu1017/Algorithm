from collections import deque
import sys

def dfs(idx):
    dfs_visited[idx] = True
    dfs_result.append(idx)

    for next in range(1, n + 1):
        if not dfs_visited[next] and graph[idx][next]:
            dfs(next)

def bfs(idx):
    q = deque([idx])
    bfs_visited[idx] = True
    bfs_result.append(idx)

    while q:
        v = q.popleft()
        for next in range(1, n + 1):
            if not bfs_visited[next] and graph[v][next]:
                q.append(next)
                bfs_visited[next] = True
                bfs_result.append(next)

count = 0
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n+1)]

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
dfs_result = []
bfs_result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
bfs(v)

for i in dfs_result:
    print(i, end = ' ')

print()
for i in bfs_result:
    print(i, end = ' ')