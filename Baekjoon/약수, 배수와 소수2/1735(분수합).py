import sys

num_list = []

def GCD(x,y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

for _ in range(2):
    num_list.append(list(map(int, sys.stdin.readline().split())))

LCM_result = LCM(num_list[0][1], num_list[1][1])
child = num_list[0][0] * (LCM_result // num_list[0][1]) + num_list[1][0] * (LCM_result // num_list[1][1])
GCD_result = GCD(child, LCM_result)

if GCD_result == 1:
    print(f'{child} {LCM_result}')
else:
    print(f'{child//GCD_result} {LCM_result//GCD_result}')