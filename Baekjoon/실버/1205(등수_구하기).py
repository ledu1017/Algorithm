import sys

input = sys.stdin.readline

n, score, p = map(int, input().split())
result = 1

if n > 0:
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    if len(score_list) == p and min(score_list) < score:
        score_list.pop()
        score_list.append(score)
    elif len(score_list) == p and min(score_list) >= score:
        result = -1
    else:
        score_list.append(score)
    score_list.sort(reverse=True)

    if result != -1:
        index = [i + 1 for i, v in enumerate(score_list) if v == score]
        result = min(index)

print(result)