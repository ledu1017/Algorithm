import sys

def exist():
    for i in m_list:
        start = 0
        end = len(n_list) - 1

        while start <= end:
            middle = (start + end) // 2
            if n_list[middle] == i:
                print(n_dict.get(i))
                break
            elif n_list[middle] > i:
                end = middle -1
            else:
                start = middle + 1
        if start > end:
            print(0)
            

n_dict = {}

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline().strip())
m_list = list(map(int, sys.stdin.readline().split()))

for i in n_list:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

set_list = set(n_list)
n_list = list(set_list)
n_list.sort()

exist()