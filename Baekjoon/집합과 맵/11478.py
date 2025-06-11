import sys

result = set()
s = str(sys.stdin.readline().strip())

for i in range(1, len(s)+1):
    for j in range(len(s)):
        result.add(s[j:j+i])

print(len(result))