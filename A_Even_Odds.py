n, k = map(int, input().split())

div = (n + 1) // 2 

if k <= div:
    print(2 * k - 1)
else:
    print(2 * (k - div))
