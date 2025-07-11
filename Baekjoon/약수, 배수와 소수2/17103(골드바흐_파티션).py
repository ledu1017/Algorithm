import sys

num_list = []
result = []

def prime_num(num):
    prime = []
    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, num+1):
        j = 2

        while(i * j) <= num:
            arr[i * j] = False
            j += 1

    for i in range(2, num):
        if arr[i] == True:
            prime.append(i)
    
    return prime

x = int(sys.stdin.readline().strip())

for _ in range(x):
    num_list.append(int(sys.stdin.readline().strip()))

arr = prime_num(max(num_list))

for i in num_list:
    count = 0
    for j in arr:
        if i - j in arr:
            count += 1
    print(count)


'''
########################
# 시간 초과 발생
# 입력 값 - 소수 = 소수 라면 그게 골드바흐 파티션이 될 수 있음 그 방식으로 시도해야함
########################
import sys

num_list = []
result = []

def prime_num(num):
    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, num+1):
        j = 2

        while(i * j) <= num:
            arr[i * j] = False
            j += 1

    return arr

x = int(sys.stdin.readline().strip())

for _ in range(x):
    num_list.append(int(sys.stdin.readline().strip()))

arr = prime_num(max(num_list))

for i in num_list:
    middle = []
    for j in range(2, i + 1):
        for k in range(2, i + 1):
            if arr[j] == True and arr[k] == True and j + k == i:
                middle.append([j, k])
    normalized_pairs = {tuple(sorted(pair)) for pair in middle}    # 앞뒤 순서 바뀐거 같게 보기
    result.append(len(normalized_pairs))

for i in result:
    print(i)
'''