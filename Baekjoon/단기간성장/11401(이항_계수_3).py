import sys, math

def bino_coef_factorial(n, k):
	return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

n, k = map(int, sys.stdin.readline().split())

result = bino_coef_factorial(n, k)

if result < 1000000007:
	print(result)
else:
	print(result % 1000000007)