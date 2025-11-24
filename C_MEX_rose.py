t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    seen = [False] * (m + 1)  
    C = 0

    for num in a:
        if num == m:
            C += 1
        if num < m:
            seen[num] = True

    Z = seen[:m].count(False)

    print(max(C, Z))
