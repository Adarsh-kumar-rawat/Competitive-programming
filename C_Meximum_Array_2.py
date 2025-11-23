t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    res = []
    for __ in range(q):
        c, l, r = map(int, input().split())
        res.append((c, l - 1, r - 1))

    a = [k] * n

    mex_segs = []

    for c, l, r in res:
        if c == 2:
            mex_segs.append((l, r))
    
    for l, r in mex_segs:
        for i in range(k):
            if l + i <= r:
                a[l + i] = i
        
        for i in range(l + k, r + 1):
            if a[i] == k:
                a[i] = k + 1

    print(*a)
