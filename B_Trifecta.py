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
    n = int(input())
    arr = list(map(int, input().split()))

    new = []

    for i in range(len(arr)):
        new.append([arr[i],i])

    new.sort( key = lambda x : x[0])

    res = []

    for i in range(3):
        val = new[i][1]
        val +=1 
        res.append(val)

    print(*res)

def main():
    t = 1 
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()