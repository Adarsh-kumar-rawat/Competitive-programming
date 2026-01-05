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
    s = input()
    ans = 0 

    for ch in s:
        if ch == "Y":
            ans +=1 
    
    if ans > 1:
        print("NO")
    else:
        print("YES")

    #print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()