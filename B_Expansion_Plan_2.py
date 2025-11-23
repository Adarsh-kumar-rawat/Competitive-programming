t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    s = input()

    a = abs(x)
    b = abs(y)

    for ch in s:
        if ch == '8':
            if a > 0 and b > 0:
                a -= 1
                b -= 1
            elif a > 0:
                a -= 1
            elif b > 0:
                b -= 1
        else:  #'4'
            if a >= b and a > 0:
                a -= 1
            elif b > 0:
                b -= 1

    if a == 0 and b == 0:
        print("YES")
    else:
        print("NO")
