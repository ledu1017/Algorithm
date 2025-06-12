import sys

member = set()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    name, state = map(str, sys.stdin.readline().split())
    if state == 'enter':
        member.add(name)
    else:
        member.discard(name)

member = list(member)
member.sort(reverse=True)

for i in member:
    print(i)