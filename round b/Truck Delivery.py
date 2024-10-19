for x in range(int(input())):
    N, Q = map(int, input().split())
    info = [list(map(int, input().split())) for i in range(N-1)]
    queries = [list(map(int, input().split())) for i in range(Q)]
    print(info)
    print(queries)
    roads = {}
    for i in info:
        if i[0] not in roads:
            roads[i[0]] = [i[1]]
        else:
            roads[i[0]].append(i[1])
        if i[1] not in roads:
            roads[i[1]] = [i[0]]
        else:
            roads[i[1]].append(i[0])
    print(roads)
    def dfs(roads,i,j,toll = [], visited=set()):
        visited.add(i)
        toll.append(j)
        print(toll)
        if i==1:
            return toll
        for i in roads[i]:
            if i not in visited:
                dfs(roads, i, j,toll,visited)
    for u,v in queries:
        toll = []
        print(dfs(roads, u, v, toll))