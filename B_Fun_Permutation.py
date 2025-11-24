t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    res = []
    maxx = n 
    # make every number a multiple of 3 
    for i in range(n):
        val = n + 1 - a[i]
        res.append(val)
    print(*res)