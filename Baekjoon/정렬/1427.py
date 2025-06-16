import sys

num_list = []
num = str(sys.stdin.readline().strip())

for i in num:
    num_list.append(i)

num_list.sort(reverse=True)

for i in num_list:
    print(i, end='')