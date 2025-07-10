import sys, math

def decimal(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

x, y = map(int, sys.stdin.readline().split())

for i in range(x, y+1):
    if decimal(i) == 1 and i != 1:
        print(i)