n ,w = map(int, input().split())
product_list = [(0,0)]

for _ in range(n):
    weight, value = map(int, input().split())
    product_list.append((weight, value))

graph = [[0]*(w+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, w+1):
        weight = product_list[i][0]
        value = product_list[i][1]

        if j < weight:
            graph[i][j] = graph[i-1][j]
        else:
            graph[i][j] = max(graph[i-1][j-weight] + value, graph[i-1][j])

print(graph[n][w])