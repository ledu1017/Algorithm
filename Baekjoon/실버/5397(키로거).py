import sys
from collections import deque

input = sys.stdin.readline
result = []
n = int(input().strip())

for _ in range(n):
    l_que = deque()
    r_que = deque()
    p_list = str(input().strip())
    for i in p_list:
        if i == "<":
            if l_que:
                r_que.appendleft(l_que.pop())
        elif i == ">":
            if r_que:
                l_que.append(r_que.popleft())
        elif i == "-":
            if l_que:
                l_que.pop()
        else:
            l_que.append(i)
    result.append("".join(l_que) + "".join(r_que))

print(*result, sep='\n')