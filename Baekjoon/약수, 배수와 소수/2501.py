import sys, math

a, b = map(int, sys.stdin.readline().strip().split())

measure_list = []

for i in range(1, int(math.sqrt(a))+1):    # 중간까지만 계산
    if a % i == 0:
        measure_list.append(i)    # 약수
        measure_list.append(a//i)     # 약수 반대쪽....?

measure_list = list(set(measure_list))    # 중복 제거
measure_list.sort()    # 정렬

if len(measure_list) == 0 or len(measure_list) < b:
    print(0)
else:
    print(measure_list[b-1])