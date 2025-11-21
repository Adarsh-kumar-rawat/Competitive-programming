import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    summ = 0 
    maxx = 0 
    ans = 0
    for i in range(1,n+1):
        maxx = max(maxx , -(i*i)+i+summ)
        summ += a[i-1]
        ans = max(ans, (i*i +i -summ) + maxx)

    print(ans+summ)