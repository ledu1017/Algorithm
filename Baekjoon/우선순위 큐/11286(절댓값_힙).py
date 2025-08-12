import sys
import heapq

input = sys.stdin.readline

heap = []
result = []
n = int(input().strip())

for _ in range(n):
    num = int(input().strip())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)

print(*result, sep='\n')