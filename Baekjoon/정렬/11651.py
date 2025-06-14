import sys

num_list = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split())))

num_list.sort(key = lambda x:(x[1], x[0]))

for i in num_list:
    print(f"{i[0]} {i[1]}")