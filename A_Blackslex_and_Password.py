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
    k , x = map(int,input().split())
    print(k*x +1)

    ans = 0

    print(ans)

def main():
    t = int(input()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
