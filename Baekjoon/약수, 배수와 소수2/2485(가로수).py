import sys

num_list = []
count = int(sys.stdin.readline().strip())

for _ in range(count):
    num_list.append(int(sys.stdin.readline().strip()))

for i in num_list[1:]:
    print(i)