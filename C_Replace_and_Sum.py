import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7


def solve():
    """
    breakdown:

    first just replace whatever num in buigger in b with a right 
    after that right most biggest number we will just make everything equal to that 
    than we can make a prefix array for summ 
    """

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    for i in range(n):
        if a[i] < b[i]:
            a[i] = b[i]

    for i in range(n - 2, -1, -1):
        a[i] = max(a[i], a[i + 1])


    prefix = [0] * n

    prefix[0] = a[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + a[i]

    def compute(l, r):
        if l == 0:
            return prefix[r]
        return prefix[r] - prefix[l - 1]

    res = []
    for _ in range(q):

        l, r = map(int, input().split())
        l -= 1
        r -= 1
        res.append(compute(l, r))

    print(*res)



def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()