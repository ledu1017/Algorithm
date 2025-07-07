'''
# 가운데 값을 찾기위해 가운데 값 기준으로 왼쪽 힙은 작게, 오른쪽 힙은 크게 만들어줌
# heqppush할 때 음수를 붙이면 최대힙으로 만들 수 있음
# 왼쪽의 가장 큰 값과 오른쪽의 가장 작은 값을 비교해서 가운데값을 찾을 수 있게 함
'''
import sys, heapq

result = []
left_heap = []
right_heap = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    input_num = int(sys.stdin.readline().strip())

    if len(left_heap) == len(right_heap):   
        heapq.heappush(left_heap, -input_num)
    else:
        heapq.heappush(right_heap, input_num)

    if left_heap and right_heap and left_heap[0] * (-1) > right_heap[0]:
        left = heapq.heappop(left_heap)
        right =  heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right)
        heapq.heappush(right_heap, -left)

    result.append(left_heap[0] * -1)

for i in result:
    print(i)