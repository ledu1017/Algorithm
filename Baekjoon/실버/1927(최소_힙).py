import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []
result = []

for _ in range(n):
    x = int(input().strip())

    if x == 0 and heap:
        result.append(heapq.heappop(heap))
    elif x == 0 and not heap:
        result.append(0)
    else:
        heapq.heappush(heap, x)

print(*result, sep='\n')