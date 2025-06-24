weight = int(input())
weight_list = [-1]

for i in range(weight):
    for j in range(weight):
        if 5*i + 3*j == weight:
            weight_list = []
            weight_list.append(i+j)

weight_list.sort()
print(weight_list[0])