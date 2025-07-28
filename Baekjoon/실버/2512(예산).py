import sys

input = sys.stdin.readline
sum_list = []

n = int(input().strip())
m_list = list(map(int, input().split()))
max_m = int(input().strip())

start, result = 0, 0
end = max(m_list)

if sum(m_list) <= max_m:
    print(max(m_list))
else:
    while start <= end:
        result = 0
        middle = (start + end) // 2
        for i in m_list:
            if i <= middle:
                result += i
            else:
                result += middle

        if result <= max_m:
            start = middle + 1
        else:
            end = middle - 1
    print(end)