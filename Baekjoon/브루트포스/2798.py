def cal(num_list, hap):
    result = 0
    for i_idx, i in enumerate(num_list):
        for j_idx, j in enumerate(num_list[i_idx+1:-1]):
            for k in num_list[i_idx + j_idx + 2:]:
                proce = i + j + k
                if proce <= hap and result <= proce:
                    result = proce
    print(result)

count, hap = map(int, input().split())
num_list = list(map(int, input().split()))
cal(num_list, hap)