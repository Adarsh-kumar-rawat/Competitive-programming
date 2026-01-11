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
    n, w = map(int, input().split())
    arr = list(map(int, input().split()))

    mod = 2*w
    sums = [0]*mod

    for i in range(n):
        sums[i % mod] += arr[i]

    window_sum = sum(sums[:w])
    res = window_sum

    for i in range(1, mod):
        window_sum = window_sum - sums[i-1] + sums[(i + w - 1) % mod]
        res = min(res, window_sum)

    print(res)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()