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

    frong can jump from x to x i step 
    it can land between any of the value in this range 

    but before everyy jumpp 
    he goes back y units 

    so basically it jumps from 

    x - y to ( x- y +i )
    range 

    to find - min rollback to reach a number 

    the rollback curse triggers at every multyiple of bi 
    -1 if not possible 


    if after each rollback we end up in a smaller or pos than before than we say it's not possible 
    """

    n , x = map(int , input().split())

    free_dist = 0
    best_gain = 0

    for _ in range(n):
        a, b, c = map(int, input().split())
        free_dist = min(x, free_dist + (b - 1) * a)
        gain = b * a - c
        if gain > 0:
            best_gain = max(best_gain, gain)

    if free_dist >= x:
        print(0)
        return

    if best_gain == 0:
        print(-1)
        return

    remaining = x - free_dist
    rollbacks = (remaining + best_gain - 1) // best_gain
    print(rollbacks)

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()