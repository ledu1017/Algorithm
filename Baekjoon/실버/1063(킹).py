import sys
input = sys.stdin.readline

k, r, t = input().split()
t = int(t)

n = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
m = ['1', '2', '3', '4', '5', '6', '7', '8']

# 킹, 돌 좌표를 숫자 인덱스로 변환
kn, km = n.index(k[0]), m.index(k[1])
rn, rm = n.index(r[0]), m.index(r[1])

# 방향 딕셔너리
moves = {
    'R':  (1, 0),
    'L':  (-1, 0),
    'B':  (0, -1),
    'T':  (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

for _ in range(t):
    move = input().strip()
    dx, dy = moves[move]

    nkx, nky = kn + dx, km + dy  # 킹의 다음 위치

    # 킹이 체스판 밖이면 무시
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    # 킹이 돌과 겹치면 돌도 이동
    if nkx == rn and nky == rm:
        nrx, nry = rn + dx, rm + dy
        # 돌이 체스판 밖이면 명령 무시
        if not (0 <= nrx < 8 and 0 <= nry < 8):
            continue
        rn, rm = nrx, nry

    kn, km = nkx, nky  # 킹 이동

# 좌표를 다시 문자열로 변환
print(n[kn] + m[km])
print(n[rn] + m[rm])