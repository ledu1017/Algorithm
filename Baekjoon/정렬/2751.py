import sys

num = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    num.append(int(sys.stdin.readline().strip()))

num.sort()

for i in num:
    print(i)