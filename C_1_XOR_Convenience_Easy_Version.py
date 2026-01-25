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

    x _ _ _ _ _ x 
    phli , last value se koi fark nahi padta 
    but last value kisi na kisi ke equal honi chahiye 

    """

    n = int(input())
    print(*range(n, 0, -1))

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()