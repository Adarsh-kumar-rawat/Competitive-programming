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
    so the ans lie between either 1 or the max sword so binary searchhh maybe 
    just keep chceking 
    compute monsters can kill with prefix summ 
    """

    n = int(input())
    swords = list(map(int, input().split()))
    mons = list(map(int, input().split()))

    swords.sort()

    pref = [0] * n
    pref[0] = mons[0]
    for i in range(1, n):
        pref[i] = pref[i-1] + mons[i]

    ans = 0

    for candidate in swords:

        pos = bisect.bisect_left(swords, candidate)
        useable = n - pos

        kills = bisect.bisect_right(pref, useable)

        ans = max(ans, kills * candidate)

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()