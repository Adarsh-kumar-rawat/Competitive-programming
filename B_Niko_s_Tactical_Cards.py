t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    k = 0 
    ans = 0 
    i = 0 
    while i < len(a):
        val1 = k - a[i]
        val2 = b[i] - k 
        candidate = max(val1,val2)
        if abs(candidate) == b[i]:
            k += b[i]
        else:
            k += a[i]
        i +=1 
        
    print(k)

    #print(a)
    #print(b)