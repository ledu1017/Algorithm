def cal(sides):
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        print("Invalid")
    elif sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")

while True:
    sides = list(map(int, input().split()))
    if sum(sides) == 0:
        break
    cal(sides)
