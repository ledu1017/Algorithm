from collections import deque
import sys

def bfs(sx, sy, m, n):
    q = deque([(sx, sy)])

    while q:
        vx, vy = q.popleft()
        visited[vx][vy] = 1

        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = vx + x, vy + y
            '''
            # 예를 들어 0,0 이랑 0,1 에서 둘 다 1,1 을 갈 수 있음
            # (nx, ny) not in q 이게 없으면 1,1이 두번 들어가서 시간 초과가 발생함
            '''
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1 and (nx, ny) not in q:
                q.append((nx, ny))

t = int(sys.stdin.readline().strip())
answer = []

for i in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for x in range(m):
        for y in range(n):
            if visited[x][y] == 0 and graph[x][y] == 1:
                count += 1
                bfs(x, y, m, n)
    answer.append(count)

print(*answer, sep='\n')

'''
# 시간초과
from collections import deque
import sys

def bfs(sx, sy, idx, m, n):
    q = deque([(sx, sy)])

    while q:
        vx, vy = q.popleft()
        visited[idx][vx][vy] = 1

        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = vx + x, vy + y
            #print(nx, ny)
            if 0 <= nx < m and 0 <= ny < n and visited[idx][nx][ny] == 0 and graph[idx][nx][ny] == 1:
                q.append((nx, ny))

t = int(sys.stdin.readline().strip())
graph = [[] * t for _ in range(t)]
visited = [[] * t for _ in range(t)]
answer = []

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph[i] = [[0] * n for _ in range(m)]
    visited[i] = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[i][x][y] = 1

for idx, i in enumerate(graph):
    count = 0
    for x in range(len(i)):
        for y in range(len(i[0])):
            if visited[idx][x][y] == 0 and graph[idx][x][y] == 1:
                count += 1
                print(x, y)
                bfs(x, y, idx, len(i), len(i[0]))
    answer.append(count)

print(*answer, sep='\n')
'''