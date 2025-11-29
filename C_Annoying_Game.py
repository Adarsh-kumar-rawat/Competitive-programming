import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = (k + 1) // 2
    y = k // 2
    net = x - y

    left = [0]*n
    cur = -10**30
    for i in range(n):
        cur = a[i] if i == 0 else max(a[i], cur + a[i])
        left[i] = cur

    right = [0]*n
    cur = -10**30
    for i in reversed(range(n)):
        cur = a[i] if i == n-1 else max(a[i], cur + a[i])
        right[i] = cur

    base = max(left)
    ans = base
    for i in range(n):
        ans = max(ans, left[i] + net * b[i] + (right[i] - a[i]))

    print(ans)
