import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
1 , 0 se - 1 
1 , 1 se - 0 

0 - alice win 
1 - bob win 

phla 0 - 2nd last 0 -> 1 1 - 0 

1la 0 end bhi zero - bob 
1 la 1 akjhri 1 - alice 
1 la 1 akhri 0 , second last - 1 
"""

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if arr[0] == 1 or arr[-1] == 1:
        print("Alice")
    else:
        print("Bob")
def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()