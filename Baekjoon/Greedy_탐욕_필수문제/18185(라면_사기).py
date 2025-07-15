'''
import sys

price = 0
n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for idx, i in enumerate(num_list):
    while(num_list[idx] != 0):
        if num_list[idx] != 0 and num_list[idx + 1] != 0 and num_list[idx + 2] != 0:
            min_value = min(num_list[idx], num_list[idx + 1], num_list[idx + 2])
            price += (min_value * 7)
            num_list[idx] -= min_value
            num_list[idx + 1] -= min_value
            num_list[idx + 2] -= min_value
        elif num_list[idx] != 0 and num_list[idx + 1] != 0:
            min_value = min(num_list[idx], num_list[idx + 1], num_list[idx + 2])
            price += (min_value * 5)
            num_list[idx] -= min_value
            num_list[idx + 1] -= min_value
        else:
            price += num_list[idx] * 3
            num_list[idx] -= num_list[idx]

print(num_list)
print(price)
'''
import sys

price = 0
n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    while num_list[i] > 0:
        # 3개 연속이 가능할 경우
        if i + 2 < n and num_list[i+1] > 0 and num_list[i+2] > 0:
            min_val = min(num_list[i], num_list[i+1], num_list[i+2])
            num_list[i] -= min_val
            num_list[i+1] -= min_val
            num_list[i+2] -= min_val
            price += 7 * min_val
        # 2개 연속이 가능할 경우
        elif i + 1 < n and num_list[i+1] > 0:
            min_val = min(num_list[i], num_list[i+1])
            num_list[i] -= min_val
            num_list[i+1] -= min_val
            price += 5 * min_val
        # 혼자만 남은 경우
        else:
            price += 3 * num_list[i]
            num_list[i] = 0

print(price)