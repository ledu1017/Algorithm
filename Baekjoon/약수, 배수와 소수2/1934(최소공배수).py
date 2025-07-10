import sys, math

num = []
result = []

n = int(sys.stdin.readline().strip())
for _ in range(n):
    num.append(list(map(int, sys.stdin.readline().split())))

for i in num:
    print(math.lcm(i[0], i[1]))