import sys, math

def cal(n, result):
    for i in range(2, int(math.sqrt(n)) + 1):
        # 나누어 떨어지면 소인수로 추가
        while n % i == 0:
            result.append(i)
            n = n // i  # 나눈 값을 다시 n에 저장
    if n > 1:  # n이 1보다 크면 마지막 남은 소인수
        result.append(n)

result = []
n = int(sys.stdin.readline().strip())

cal(n, result)

for num in result:
    print(num)