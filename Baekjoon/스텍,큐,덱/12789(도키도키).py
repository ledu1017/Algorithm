import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
result = 1
l_num, r_num, ticket = 0, 0, 0
left = deque()
right = deque(map(int, input().split()))

while left or right:
    if right: r_num = right[0]
    if left: l_num = left[-1]

    if ticket + 1 == r_num:
        ticket += 1
        right.popleft()
    elif ticket + 1 == l_num:
        ticket += 1
        left.pop()
    else:
        try:
            left.append(right.popleft())
        except:
            result = 0
            break

if result == 1:
    print("Nice")
else:
    print("Sad")