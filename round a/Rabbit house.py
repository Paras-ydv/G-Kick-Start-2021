T = int(input())
for x in range(T):
    R, C = map(int, input().split())
    grid = [list(map(int, input().split()[:C])) for i in range(R)]
    print(grid)
    max_value = max([max(i) for i in grid])
    max_values = []
    for i in grid:
        for j in range(len(i)):
            if max_value==i[j]:
                max_values.append((max_value,grid.index(i),j))
    print(max_value, max_values)