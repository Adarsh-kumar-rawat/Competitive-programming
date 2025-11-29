t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    x = 0 
    for i, j in enumerate(b):
        if j !=0:
            x = i 
            break
    #print(n)
    #print("b",b)
    if b[x] == b[-1]:
        print(1)
    else:
        ans = (n - (x+1)) +1 
        print(ans) 
