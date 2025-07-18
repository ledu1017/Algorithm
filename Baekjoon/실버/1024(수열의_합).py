import sys

n, l = map(int, sys.stdin.readline().split())
dp = [[0] * ((n // 2) + 1) for _ in range((n//2)+1)]
answer = []

for i_idx, i in enumerate(dp):
    sum = 0
    for j_idx, j in enumerate(i[i_idx:]):
        sum += j_idx + i_idx
        if sum <= 18:
            dp[i_idx][j_idx + i_idx] = sum

for i in dp:
    result = []
    if n in i:
        for idx, j in enumerate(i):
            if j != 0:
                result.append(idx)
    if result:
        answer.append(result)

answer.sort(key = len)
print(*answer[0], sep = ' ')