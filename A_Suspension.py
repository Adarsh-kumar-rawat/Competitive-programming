t = int(input())

for _ in range(t):
    n = int(input())
    y,r = map(int,input().split())
    x = y//2 

    if r >=n:
        print(r)
    else:
        res = (r + (y//2))
        if res <= n:
            print(res)
        else:
            print(n)