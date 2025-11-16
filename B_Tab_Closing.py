t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    count = 0
    while n:
        tab = min(b,a/n)
        if tab == b:
            break           
        else:
            count += 1
        n -= 1            

    print(count+1)
