import sys

n, m = map(int, sys.stdin.readline().split())
s = ()
r = []
count = 0

for _ in range(n):
    s += (str(sys.stdin.readline().strip()), )

for _ in range(m):
    r.append(str(sys.stdin.readline().strip()))

for i in r:
    if i in s:
        count += 1

print(count)