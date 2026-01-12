import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

# breakdown:
#
#

def solve():
    s, k, m = map(int, input().split())

    rem = s
    last = 0
    flips = m // k

    for i in range(min(flips, 2)):
        t = (i + 1) * k
        rem = max(0, rem - (t - last))
        rem = s - rem
        last = t

    if flips > 2:
        extra = flips - 2

        pairs = extra // 2
        last += pairs * 2 * k


        if extra % 2 == 1:
            t = last + k
            rem = max(0, rem - (t - last))
            rem = s - rem
            last = t

    rem = max(0, rem - (m - last))
    print(rem)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()