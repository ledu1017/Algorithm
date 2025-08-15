import sys

input = sys.stdin.readline

n = int(input().strip())
student = [input().strip() for _ in range(n)]
cut = {}
cut_index = 0

while len(cut) != n:
    cut_index -= 1
    cut = {}
    for i in student:
        if i[cut_index:] not in cut.keys():
            cut[i[cut_index:]] = 1

print(abs(cut_index))