import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

stack = deque()
result = []

for _ in range(n):
    order = list(map(int, input().split()))

    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif order[0] == 3:
        result.append(len(stack))
    elif order[0] == 4:
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif order[0] == 5:
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print(*result, sep='\n')