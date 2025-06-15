import sys

result = {}
n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

dist_list = sorted(set(num_list))

for idx, i in enumerate(dist_list):
    result[i] = idx

for i in num_list:
    print(result[i], end=' ')