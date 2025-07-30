'''
# 그래프를 그려서 홀수일때는 무조건 결과가 1개인걸 알 수 있음
# 짝수일때도 그래프를 그리면 최소가 나올때를 알 수 있다고 함
# 그런데 잘 이해가 안가서 그냥 외웠음
# https://v3.leedo.me/devs/58
'''

import sys

input = sys.stdin.readline

n = int(input().strip())
time = []

for _ in range(n):
    a, b = map(int, input().split())
    time.append(b - a)

time.sort()

if len(time) % 2 == 0:
    start = len(time) // 2
    count = time[start] - time[start - 1] + 1
    print(count)
else:
    print(1)


'''
# 답은 나오지만 메모리 초과 발생
import sys

n = int(sys.stdin.readline().strip())
time = []
delay = []
count = 0

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))    # 시간 입력 받음

for i in time:
    delay.append(i[1] - i[0])    # 각 시간들의 딜레이 계산해서 저장

size = (abs(max(delay) - min(delay)) + 1)
graph = [0] * size

if n == 1:
    graph[0] = 1
else:
    for i in range(min(delay), max(delay) + 1):    # 딜레이 시킬 수 있는 시간중 가장 작은 시간부터 가장 큰 수를 반복하며 딜레이 시켰을 때 기다리는 시간을 구할 수 있음
        for j in time:
            graph[count] += abs(j[0] + i - j[1])
        count += 1
    
min_value = min(graph)
print(graph.count(min_value))
'''