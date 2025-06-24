def cal(input_list):
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if input_list[0] * i + input_list[1] * j == input_list[2] and input_list[3] * i + input_list[4] * j == input_list[5]:
                print(i, j)
                break
            
input_list = list(map(int, input().split()))
cal(input_list)