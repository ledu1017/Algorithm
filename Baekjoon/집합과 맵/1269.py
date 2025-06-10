import sys

n,m = map(int, sys.stdin.readline().split())

set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))

print(len(set_a.difference(set_b)) + len(set_b.difference(set_a)))