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

    n , k = map(int , input().split())

    if k > n :
        print(-1)
    if k == n:
        print(0)

    time = 0 

    while n > k :
        if n % 2 == 0 :
            n = n//2
            time += 1 

        if n % 2 != 0:
            n = n//2
            time += 1
            a = n+1
            b = n 

            if a == k or b == k:
                print(time)
                break 
            n = a 
        
        if n < k :
            print(-1)
            break

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()