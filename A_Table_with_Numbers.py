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

    n, h, l = map(int, input().split())
    arr = list(map(int, input().split()))

    a = 0 
    b = 0  
    o = 0  

    m = min(h, l)

    for x in arr:
        if x <= h:
            a += 1
        if x <= l:
            b += 1
        if x <= m:
            o += 1

    c = b - o  

    if a <= c :
        print(a)
    else:
        print(min(b, (a + c) // 2))



def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()