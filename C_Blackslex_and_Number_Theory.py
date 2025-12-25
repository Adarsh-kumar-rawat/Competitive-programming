import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
breakdownn : 
valid ans will either be the smallest number itself - to get 0 
or anything +1 to get the number itself 
"""

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    val1 = arr[0]
    val2 = arr[1]

    def valid(num, r):
        possible = []
        for x in range(r + 1, num + 1):
            if num % x == r:
                possible.append(x)
        return possible

    for i in range(1,len(arr)):
        x = valid(arr[i], val1)
        if len(x) == 0:
            print(val1)
            break
    else:
        nums = valid(val2, val1)
        ans = nums[-1]
        print(ans)

def main():
    t = int(input()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
