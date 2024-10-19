for x in range(int(input())):
    N, C = map(int, input().split())
    intervals = []
    for i in range(N):
        intervals.append(list(map(int, input().split())))