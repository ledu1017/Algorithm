import sys

a, b= -1, -1
input_list = []

while a and b !=0:
    a,b = map(int, sys.stdin.readline().strip().split())
    input_list.append([a,b])

for num in input_list:
    if num[0] > num[1]:
        if num[0] % num[1] == 0:
            print("multiple")
        else:
            print("neither")
    elif num[0] < num[1]:
        if num[1] % num[0] == 0:
            print("factor")
        else:
            print("neither")
    else:
        break