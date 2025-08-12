import sys
import heapq

input = sys.stdin.readline

t = int(input().strip())
result = []

for _ in range(t):
    m = int(input().strip())
    left = []
    right = []
    middle = []
    num_list = []

    while len(num_list) < m:
        line = input().strip()
        numbers = list(map(int, line.split()))
        num_list.extend(numbers)

    for idx, i in enumerate(num_list):
        if len(left) == len(right):
            heapq.heappush(left, -i)
        else:
            heapq.heappush(right, i)
        
        if right and -left[0] > right[0]:
            max_left = heapq.heappop(left)
            min_right = heapq.heappop(right)

            heapq.heappush(left, -min_right)
            heapq.heappush(right, -max_left)

        if (idx + 1) % 2 != 0:
            middle.append(-left[0])
    
    result.append(middle)

for middle in result:
    print(len(middle))
    for i in range(0, len(middle), 10):
        print(*middle[i:i+10])