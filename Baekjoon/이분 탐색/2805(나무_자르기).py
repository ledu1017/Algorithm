import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

result = 0
start = 0
end = max(tree)

while start <= end:
    result = 0
    middle = (start + end) // 2
    
    for i in tree:
        if i - middle > 0:
            result += i-middle
    
    if result < m:
        end = middle - 1
    else:
        start = middle + 1

print(end)