import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect


INF = 10**18
MOD = 10**9 + 7

"""
breakdownn : 

must output - arr of 2^n
array will contain everthing till 2^n -1 

"""

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    print(ans)

def main():
    t = int(input()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
