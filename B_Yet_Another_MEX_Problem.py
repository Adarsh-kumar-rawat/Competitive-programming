import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
k window , 

in the end array mei 

operation number = n-k +1 
har operation mei 1 element hat jayga 
goal - to mimimize mex 




"""

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = defaultdict(int)
    mex_list = []

    for i in range(k):
        freq[arr[i]] += 1

    mex = 0
    while freq[mex] > 0:
        mex += 1
    mex_list.append(mex)

    for i in range(k, n):
        out = arr[i - k]
        freq[out] -= 1

        in_elem = arr[i]
        freq[in_elem] += 1

        if out < mex and freq[out] == 0:
            mex = out
        while freq[mex] > 0:
            mex += 1

        mex_list.append(mex)
    
    print(mex_list)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()