import sys, math

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
result = []

for num in range(m, n+1):
    check = 0
    for i in range(2, int(math.sqrt(num) +1)):
        if num % i == 0:
            check = 1
            break
    if check == 0 and num != 1:
        result.append(num)

if sum(result) > 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)