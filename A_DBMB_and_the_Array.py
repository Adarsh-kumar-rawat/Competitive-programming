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
    """
    n, s, x = map(int, input().split())
    arr = list(map(int, input().split()))

    su = sum(arr)

    if su == s:
        print("YES")
        return

    if su > s:
        print("NO")
        return

    diff = s - su

    if diff % x == 0:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()