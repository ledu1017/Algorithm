import sys

def cut():
    start = 1
    end = max(cable)

    while start <= end:
        count = 0
        middle = (start + end) // 2

        for i in cable:
            count += i // middle

        if count < n :
            end = middle - 1
        else:
            start = middle + 1
        
    return end

k, n = map(int, sys.stdin.readline().split())
cable = []
result = []

for _ in range(k):
    cable.append(int(sys.stdin.readline().strip()))

cable.sort()

print(cut())