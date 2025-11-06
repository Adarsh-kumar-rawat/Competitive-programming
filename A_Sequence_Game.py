t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    i = 0
    while i < len(a) - 1:
        if min(a[i], a[i+1]) <= x <= max(a[i], a[i+1]):
            a.pop(i)      
            a.pop(i)      
            a.insert(i, x) 
            if i > 0:
                i -= 1
        else:
            i += 1  

    if len(a) == 1 and a[0] == x:
        print("YES")
    else:
        print("NO")
