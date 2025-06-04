from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[] for _ in range(n+1)]
bfs_list = [0] * (n+1)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1): # 인접노드 정보 오름차순 정렬
    graph[i].sort()

def bfs(v):
    count = 1
    q = deque([v])
    bfs_list[v] = count

    while q:
        v = q.popleft()
        for i in graph[v]:
            if bfs_list[i] == 0:
                q.append(i)
                count += 1
                bfs_list[i] = count
    
    for i in bfs_list[1:]:
        print(i)

bfs(v)