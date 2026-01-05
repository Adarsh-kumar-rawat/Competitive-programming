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
    
    prefix = [0]
    val = 0
    su = 0
    curr = arr[0]
    for i in range(1,len(arr)):
        su -= arr[i]











        
        val += abs(arr[i])
        prefix.append(val)

    #print("prefix",prefix)

    mx = su

    for i in range(1,len(arr)):
        su += arr[i]
        curr = su + prefix[i-1]
        mx = max(mx,curr)

        curr = arr[0]

    print(mx)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()