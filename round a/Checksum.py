T = int(input())
for x in range(T):
    N = int(input())
    A = [list(map(int, input().split()[:N])) for i in range(N)]
    B = [list(map(int, input().split()[:N])) for i in range(N)]
    R = list(map(int, input().split()[:N]))
    C = list(map(int, input().split()[:N]))
    print(A)
    print(B)
    print(R)
    print(C)
    min_one_cnt = {}
    info = {}
    min_one_colwise = []
    for i in range(N):
        count = 0
        for j in range(N):
            if A[j][i]==-1:
                count+=1
        min_one_colwise.append(count)
    for i in range(N):
        for j in range(N):
            if A[i][j]==-1:
                info[(i,j)] = [A[i].count(-1),min_one_colwise[j],B[i][j]]
    print(info)
    sorted_info = {}
    for key, value in info.items():
        

    '''for i in range(len(A)):
        min_one_cnt[i+1] = A[i].count(-1)
    print(min_one_cnt)
    sorted_min_one_cnt = {}
    for key in sorted(min_one_cnt, key=min_one_cnt.get):
        sorted_min_one_cnt[key] = min_one_cnt[key]
    print(sorted_min_one_cnt)
    for key, value in sorted_min_one_cnt.items():
        if value==0:
            continue
        #else:'''

    
        