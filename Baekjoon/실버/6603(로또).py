import sys
from itertools import combinations

input = sys.stdin.readline
result = []

while(True):
    num_list = list(map(int, input().split()))
    if num_list[0] == 0:
        result.pop()
        break
    for num in combinations(num_list[1:], 6):
        result.append(num)
    result.append('\n')

for i in result:
    for j in i:
        if j != '\n':
            print(j, end =' ')
        else:
            print()
    if i != '\n':
        print()