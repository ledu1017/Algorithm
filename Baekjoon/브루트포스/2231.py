#import sys

def cal(input):
    proce = input
    result = 0
    while proce > proce // 2:
        if input == proce + sum(map(int, str(proce))):
            result = proce
        proce -= 1
    return result

#print(cal(int(sys.stdin.readline().rstrip())))
print(cal(int(input())))