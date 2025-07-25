import sys
from collections import deque

def bfs(sx, sy):
    global visited
    visited[sx][sy] = 1
    q = deque([(sx, sy)])

    while q:
        vx, vy = q.popleft()
        for x, y in ((-1,0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1,0), (1,-1), (1,1)):
            nx, ny = vx + x, vx + y
            if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] == 0 and graph[ny][nx] == 1 and (nx, ny) not in q:
                visited[ny][nx] = visited[vy][vx] + 1
                q.append((nx, ny))
    print(visited)

input = sys.stdin.readline
land = []

while(True):
    w, h = map(int, input().split())
    count = 0
    graph = []

    if w == 0 and h == 0:
        break

    for _ in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[0] * w for _ in range(h)]

    bfs(0, 0)