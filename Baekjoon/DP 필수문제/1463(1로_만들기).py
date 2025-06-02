'''
# 동적 프로그래밍은 모든 경우의수를 확인하는거 같으니 대부분 배열에 값을 넣어서 구한다고 생각하면 될 듯
# 이전 값에 계산을 한다고 보면 될듯?
'''
import sys

n = int(sys.stdin.readline().strip())

count = [0] * (n+1)

for i in range(2, n+1):
    count[i] = count[i-1] + 1
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3] + 1)
    if i % 2 == 0:
        count[i] = min(count[i], count[i//2] + 1)

print(count[n])