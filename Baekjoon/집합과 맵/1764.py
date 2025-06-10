import sys

set_a = set()
set_b = set()

n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    set_a.add(str(sys.stdin.readline().strip()))

for _ in range(m):
    set_b.add(str(sys.stdin.readline().strip()))

result = list(set_a & set_b)
result.sort()

print(len(result))
for i in result:
    print(i)