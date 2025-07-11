'''
유클리드 호재법으로 구하는 최소공배수 & 최대공약수
'''
import sys

x, y = map(int, sys.stdin.readline().split())

def GCD(x, y):
    while(y):
        x,y = y, x%y
    return x

def LCM(x, y):
    result = (x*y)//GCD(x, y)
    return result

print(LCM(x, y))