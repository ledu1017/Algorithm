import sys, math

num_list = []
middle_result = []
measure_list = []
result_list = []

while True:
    a = int(sys.stdin.readline().strip())
    if a == -1:
        break
    num_list.append(a)

for num in num_list:
    middle_result = []
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            middle_result.append(i)
            middle_result.append(num // i)
    measure_list = list(set(middle_result))
    measure_list.sort()
    result_list.append(measure_list)

for idx, group in enumerate(result_list):
    group = group[:-1]
    if sum(group) == num_list[idx]:
        print(f"{num_list[idx]} = ", end='')
        print(" + ".join(map(str, group)))
    else:
        print(f"{num_list[idx]} is NOT perfect.")