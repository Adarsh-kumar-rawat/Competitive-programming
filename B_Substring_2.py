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

    n , m = map(int,input().split())
    t = input()
    s = input()

    if s in t:
        print(0)
        return 
    

    t = list(t)
    s = list(s)

    ans = 0 
    mn = float("-inf")

    for i in range(n,m):
        


def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()