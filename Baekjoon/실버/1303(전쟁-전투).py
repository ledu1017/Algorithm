import sys
from collections import deque

def bfs(x, y, soldier):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    count = 1

    while q:
        vx, vy = q.popleft()
        for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
            nx, ny = vx + dx, vy + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny] and graph[nx][ny] == soldier:
                    visit[nx][ny] = 1
                    count += 1
                    q.append((nx, ny))
    return count ** 2

input = sys.stdin.readline
n, m = map(int, input().split())  # n: 가로, m: 세로
graph = [list(input().strip()) for _ in range(m)]
visit = [[0] * n for _ in range(m)]

w_power = 0
b_power = 0

for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            soldier = graph[i][j]
            power = bfs(i, j, soldier)
            if soldier == 'W':
                w_power += power
            else:
                b_power += power

print(w_power, b_power)