T = int(input())
for x in range(T):
    N, Q, P = map(int, input().split())
    array = list(map(int, input().split()))
    print(array)
    queries = []
    res = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    print(queries)
    for i in queries:
        if i[0]==1:
            array[i[1]-1] = i[2]
        else:
            sum = 0
            prime_factors = []
            for j in range(i[2]-1,i[3]):
                x = array[j]**i[1] - (array[j]%P)**i[1]
                while (x%P==0 and x!=0):
                    print(x)
                    sum += 1
                    x = x/P
            res.append(sum)
    print(res)