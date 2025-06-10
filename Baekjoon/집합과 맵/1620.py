import sys

result = []
answer = []
pocket = dict()
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    pocket[str(i+1)] = str(sys.stdin.readline().strip())

pocket_reverse = dict(map(reversed, pocket.items()))


for _ in range(m):
    answer.append(str(sys.stdin.readline().strip()))

for i in answer:
    if i in pocket.keys():
        print(pocket[i])
    else:
        print(pocket_reverse[i])