'''
strictly increasing sequence +ve int
ai <a2 ... 
to fine - x and y 
such that x < y 
and y mod x is even 

if satisy return x and y , else return -1 


'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    found = False
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[j] % a[i] % 2 == 0:
                print(a[i], a[j])
                found = True
                break
        if found:
            break
    
    if not found:     #I KNOw THIS WILL GIVE TLE BUT LESS JUS TRY
        print(-1)
