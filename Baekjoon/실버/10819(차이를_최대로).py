import sys
from itertools import permutations

input = sys.stdin.readline

max_num = 0
n = int(input().strip())
num_list = list(map(int, input().split()))

for num in permutations(num_list):
    result = 0
    for idx, i in enumerate(num[:-1]):
        result += abs(i - num[idx + 1])
    max_num = max(result, max_num)
    
print(max_num)