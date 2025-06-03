from collections import deque
import sys

def bfs(sx, sy):
    q = deque([(sx, sy)])

    while q:
        vx, vy = q.popleft()

        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = vx + x, vy + y
            if 0 <= nx < m and 0 <= ny <n and visited[ny][nx] == 0 and graph[ny][nx] == 1 and (nx, ny) not in q:
                visited[ny][nx] = visited[vy][vx] + 1
                q.append((nx, ny))

n, m = map(int, sys.stdin.readline().split())
graph = [[] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().strip()))

visited[0][0] = 1
bfs(0, 0)

print(visited[n-1][m-1])