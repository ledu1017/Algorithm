import sys

num_list = []
result = []

def prime_num(num):
    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, num + 1):
        if arr[i] == True:
            j =2

            while(i * j) <= num:
                arr[i * j] = False
                j += 1

    return arr

while(True):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        break
    else:
        num_list.append(a)

arr = prime_num(max(num_list) * 2)

for i in num_list:
    count = 0
    for j in range(i + 1, (i * 2) + 1):
        if arr[j] == True:
            count += 1
    result.append(count)

for i in result:
    print(i)




'''
########################
# 아래 방법은 시간 초과 발생함.
########################
import sys, math

num_list = []
result = []

def decimal(x, y):
    count = 0
    for i in range(x+1, y+1):
        check = 0
        for j in range(2, int(math.sqrt(i))+ 1 ):
            if i % j == 0:
                check = 1
                break
        if check == 1:
            continue
        elif check != 1 and i != 1:
            count += 1
    return count

while(True):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        break
    else:
        num_list.append(a)

for i in num_list:
    result.append(decimal(i, 2 * i))

for i in result:
    print(i)
'''