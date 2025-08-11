import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input().strip())

for j in range(n):
    num = list(map(int, input().split()))
    for i in num:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            heapq.heappushpop(heap, i)

print(heap[0])