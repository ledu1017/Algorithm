'''
cursor를 두고 인텍스로 구분하면 시간 초과가 발생함
그래서 left right 를 구분하고 pop append 하는 형식으로 바꿈
'''
import sys
from collections import deque

input = sys.stdin.readline
l_text = deque(input().strip())
r_text = deque()

count = int(input())


for i in range(count):
    order = list(map(str, input().split()))
    
    if order[0] == 'L' and l_text:
        r_text.appendleft(l_text.pop())
    elif order[0] == 'D' and r_text:
        l_text.append(r_text.popleft())
    elif order[0] == 'B' and l_text:
        l_text.pop()
    elif order[0] == 'P':
        l_text.append(order[1])

print("".join(l_text) + "".join(r_text))

'''
import sys

input = sys.stdin.readline

text = input()
count = int(input())

cursor = len(text) - 1

for i in range(count):
    order = list(map(str, input().split()))

    if (order[0] == 'L' and cursor == 0) or (order[0] == 'R' and cursor == len(text) - 1):
        continue
    
    if order[0] == 'L' and cursor > 0:
        cursor -= 1
    elif order[0] == 'D' and cursor < len(text) - 1:
        cursor += 1
    elif order[0] == 'B' and cursor > 0:
        text = text[:cursor - 1] + text[cursor:]
        cursor -= 1
    elif order[0] == 'P':
        text = text[:cursor] + order[1] + text[cursor:]
        cursor += 1
print(text.strip())
'''