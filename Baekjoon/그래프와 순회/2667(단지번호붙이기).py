from collections import deque
import sys

def bfs(sx, sy):
    count = 0
    q = deque([(sx, sy)])

    while q:
        vx, vy = q.popleft()
        visited[vx][vy] = 1

        for x, y in ((-1,0), (1, 0), (0, -1), (0, 1)):
            nx, ny = vx + x, vy + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
                
    if count != 0:
        return count


n = int(sys.stdin.readline().strip())
graph = []
visited = [[0] * n for _ in range(n)]
answer = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            answer.append(bfs(x, y))

answer.sort()
print(len(answer), *answer, sep='\n')