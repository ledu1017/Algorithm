import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().strip())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]

min_diff = 1000000001

# 모든 부분집합 조합 (1개 이상)
for i in range(1, n+1):
    for subset in combinations(ingredients, i):
        s = 1  # 신맛 곱
        b = 0  # 쓴맛 합
        for sour, bitter in subset:
            s *= sour
            b += bitter
        min_diff = min(min_diff, abs(s - b))

print(min_diff)

'''
# 아래처럼 하면 재료를 무조건 순서대로 넣기 때문에 1, 2, 5 번째 재료를 넣었을 때 최소가 되는걸 구할 수 없음
import sys

input = sys.stdin.readline

n = int(input().strip())

m = 1000000001
taste = []
result = [[1000000002] * n for _ in range(n)]
sin = [[0] * n for _ in range(n)]
ssn = [[0] * n for _ in range(n)]

for _ in range(n):
    taste.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n - (n-i), n):
        if i == j:
            sin[i][j] = taste[i][0]
            ssn[i][j] = taste[i][1]
            result[i][j] = abs(taste[i][0] - taste[i][1])
        else:
            sin[i][j] = sin[i][j-1] * taste[j][0]
            ssn[i][j] = ssn[i][j-1] + taste[j][1]
            result[i][j] = abs((sin[i][j-1] * taste[j][0]) - (ssn[i][j-1] + taste[j][1]))

for i in result:
    if min(i) < m:
        m = min(i)

print(m)
'''