import sys, math

count = 0
number = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))

for num in num_list:
    if num == 1:
        count += 1    # 소수 아닌거 +1
        continue
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:    # 소수가 아니라면 +1 하기 위함
            count += 1
            break

print(number - count)