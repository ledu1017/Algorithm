import sys
sys.setrecursionlimit(10**6)

def dfs(idx):
    global count
    visited[idx] = count
    graph[idx].sort(reverse=True)
    for i in graph[idx]:
        if visited[i] == 0:
            count += 1
            dfs(i)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  

dfs(v)

for i in range(1, n + 1):
    print(visited[i])