t = int(input())

for _ in range(t):

    n = int(input())
    s = input().strip()

    def palin(x):
        return x == x[::-1]

    def non_dec(p):
        return all(p[i] <= p[i+1] for i in range(len(p)-1))

    # Case 1: already palindrome
    if palin(s):
        print(0)
        print()
        continue

    found = False

    for mask in range(1 << n):
        p = []
        x = []
        idx = []

        for i in range(n):
            if mask & (1 << i):
                p.append(s[i])
                idx.append(i + 1)
            else:
                x.append(s[i])

        if non_dec(p) and palin(x):
            print(len(idx))
            if idx:
                print(*idx)
            print() if not idx else None
            found = True
            break

    if not found:
        print(-1)
