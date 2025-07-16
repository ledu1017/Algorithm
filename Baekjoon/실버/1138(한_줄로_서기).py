import sys

n = int(sys.stdin.readline().strip())
key = list(map(int, sys.stdin.readline().split()))
array = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if key[i] == count and array[j] == 0:
            array[j] = i+1
            break
        elif array[j] == 0:
            count +=1


print(*array, sep=' ')