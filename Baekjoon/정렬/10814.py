import sys

n = int(sys.stdin.readline().strip())
member = []

for i in range(n):
    info = list(map(str, sys.stdin.readline().split()))
    info.append(i)
    info[0] = int(info[0])
    member.append(info)

member.sort(key = lambda x:(x[0], x[2]))

for i in member:
    print(i[0], i[1])