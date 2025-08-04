import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
num_list = deque(map(int, input().split()))
num_index = deque(i for i in range(1, n + 1))
result = []

num = num_list.popleft()
index = num_index.popleft()
result.append(index)

while num_list:
    if num > 0:
        for _ in range(num - 1):
            num_list.append(num_list.popleft())
            num_index.append(num_index.popleft())
    else:
        for _ in range(abs(num)):
            num_list.appendleft(num_list.pop())
            num_index.appendleft(num_index.pop())

    num = num_list.popleft()
    index = num_index.popleft()
    result.append(index)

print(*result, sep = ' ')