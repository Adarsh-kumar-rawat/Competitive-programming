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

    if n== 2:
        print(2)
        return 
    
    if n == 3:
        print(3)
        return 
    
    if n %2 == 0:
        print(0)
    else:
        print(1)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()