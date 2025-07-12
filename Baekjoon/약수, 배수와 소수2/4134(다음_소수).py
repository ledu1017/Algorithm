import sys, math


num_list = []

def decimal(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

count = int(sys.stdin.readline().strip())

for _ in range(count):
    num_list.append(int(sys.stdin.readline().strip()))

for i in num_list:
    check_num = i
    while(True):
        if decimal(check_num) == 1 and check_num != 0 and check_num != 1:
            print(check_num)
            break
        else:
            check_num += 1