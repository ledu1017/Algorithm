import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())

num_list = deque([])
result = []

for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] == 1:
        num_list.appendleft(order[1])
    elif order[0] == 2:
        num_list.append(order[1])
    elif order[0] == 3:
        if num_list:
            result.append(num_list.popleft())
        else:
            result.append(-1)
    elif order[0] == 4:
        if num_list:
            result.append(num_list.pop())
        else:
            result.append(-1)
    elif order[0] == 5:
        result.append(len(num_list))
    elif order[0] == 6:
        if num_list:
            result.append(0)
        else:
            result.append(1)
    elif order[0] == 7:
        if num_list:
            result.append(num_list[0])
        else:
            result.append(-1)
    elif order[0] == 8:
        if num_list:
            result.append(num_list[-1])
        else:
            result.append(-1)

print(*result, sep='\n')