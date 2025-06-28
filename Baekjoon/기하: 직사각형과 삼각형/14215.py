def cal(side):
    side.sort(reverse = True)
    if side[0] >= side[1] + side[2]:
        side[0] = side[1] + side[2] - 1
    return sum(side)

side = list(map(int, input().split()))
print(cal(side))