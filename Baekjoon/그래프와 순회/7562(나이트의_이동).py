from collections import deque
import sys

def move(sx, sy, tx, ty, size):
    q = deque([(sx, sy)])
    visited[sy][sx] = 1

    while visited[ty][tx] == 0:
        vx, vy = q.popleft()

        for x, y in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2,), (1, 2)):
            nx, ny = vx + x, vy + y
            if 0 <= nx < size and 0 <= ny < size and visited[ny][nx] == 0:
                visited[ny][nx] = visited[vy][vx] + 1
                q.append((nx, ny))

    return visited[ty][tx] - 1
        

t = int(sys.stdin.readline().strip())
answer = []

for _ in range(t):
    size = int(sys.stdin.readline().strip())
    sx, sy = map(int, sys.stdin.readline().split())
    tx, ty = map(int, sys.stdin.readline().split())

    visited = [[0] * size for _ in range(size)]
    visited[sy][sx] = 1

    answer.append(move(sx, sy, tx, ty, size))

print(*answer, sep='\n')