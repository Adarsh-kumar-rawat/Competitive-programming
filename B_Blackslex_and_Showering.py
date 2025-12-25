import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect


INF = 10**18
MOD = 10**9 + 7

"""
breakdownn : 
k alphabetsb 
(j-i) % x == 0 
si != sj



"""

def solve():

    n = int(input())
    a = list(map(int, input().split()))

    base = sum(abs(a[i] - a[i+1]) for i in range(n-1))
    best = base

    best = min(best, base - abs(a[0] - a[1]))
    best = min(best, base - abs(a[-2] - a[-1]))

    for i in range(1, n-1):
        delta = abs(a[i-1] - a[i]) + abs(a[i] - a[i+1]) - abs(a[i-1] - a[i+1])
        best = min(best, base - delta)

    print(best)

def main():
    t = int(input()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
