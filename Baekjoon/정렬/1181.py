import sys

n = int(sys.stdin.readline().strip())
word_list = []

for _ in range(n):
    word_list.append(str(sys.stdin.readline().strip()))

word_list = list(set(word_list))

word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)