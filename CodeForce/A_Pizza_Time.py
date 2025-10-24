t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    hao = 0
    while n >= 3:
        rem = n // 3
        hao += rem
        n -= 2 * rem
    print(hao)
