import sys

input = sys.stdin.readline

n = int(input().strip())
candidate = [int(input().strip()) for _ in range(n)]
candidate = [candidate[0]] + sorted(candidate[1:], reverse=True)
first = candidate[0]
count, index = 0, 1
max_len = len([i for i in candidate if i == max(candidate)])

while first != max(candidate) or max_len != 1:
    candidate[0] += 1
    candidate[index] -= 1
    count += 1
    first = candidate[0]
    candidate = [candidate[0]] + sorted(candidate[1:], reverse=True)
    max_len = len([i for i in candidate if i == max(candidate)])

print(count)