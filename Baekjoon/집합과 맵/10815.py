import sys

n = int(sys.stdin.readline().strip())
card = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')