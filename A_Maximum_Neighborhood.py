t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    elif n == 3 or n == 4:
        last = n*n 
        a = last - 1
        b = a - 1 
        c = n*(n-1) - 1
        print(last+a+b+c)
    else:
        a = (n*n)-1  
        e = n* (n-1)
        b = e - 1  # 
        c = b -1 
        d = n* (n-2) - 1
        print(a+b+c+d+e) 