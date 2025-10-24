import sys
from collections import Counter

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    f = Counter(x for x in a if x <= n)

    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + f[i]

    for g in range(n, 0, -1):
        erase = 0

        b1 = min(n, 3 * g - 1)
        total1 = p[b1]
        mults1 = f[g] + f[2 * g] if 2 * g <= n else f[g]
        erase += (total1 - mults1)

        a2 = 3 * g + 1
        b2 = min(n, 4 * g - 1)
        if a2 <= b2:
            total2 = p[b2] - p[a2 - 1]
            erase += total2

        if erase <= k:
            print(g)
            break

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
