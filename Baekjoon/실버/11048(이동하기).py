import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * (m + 1)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i][j]

print(dp[-1][-1])

'''
# 답은 나오지만 메모리 초과가 발생함
# 이 문제는 bfs가 아니라 dp 문제라고 함
# https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-11048%EB%B2%88-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-python-bfsdfs-%EA%B0%99%EC%9D%80-dp-5%EA%B0%80%EC%A7%80-%ED%92%80%EC%9D%B4
from collections import deque
import sys

def move_sum():
    q = deque([(0, 0)])

    while q:
        vx, vy = q.popleft()

        for x, y in ((1, 0), (0, 1), (1, 1)):
            nx, ny = vx + x, vy + y
            if nx < n and ny < m:
                result[nx][ny] = max(result[nx][ny], result[vx][vy] + graph[nx][ny])
                q.append((nx, ny))

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
result = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

result[0][0] = graph[0][0]
move_sum()
print(result[-1][-1])
'''