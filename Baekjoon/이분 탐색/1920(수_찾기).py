import sys

def exist():
    for i in m_list:
        start = 0
        end = len(n_list) - 1

        while start <= end:
            middle = (start + end) // 2
            if n_list[middle] == i:
                print(1)
                break
            elif n_list[middle] > i:
                end = middle -1
            else:
                start = middle + 1
        if start > end:
            print(0)


input = sys.stdin.readline
n = int(input().strip())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input().strip())
m_list = list(map(int, input().split()))

exist()