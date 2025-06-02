import sys

pibo = [0, 1]
n = int(sys.stdin.readline().strip())

def cal():
    pibo.append(pibo[-1] + pibo[-2])

for _ in range(n-1):
    cal()

print(pibo[-1])