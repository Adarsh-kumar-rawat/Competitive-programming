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

    x, y = map( int , input().split())

    while y <= x:
        y += 7 

    ans = y - x

    print(ans)

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()