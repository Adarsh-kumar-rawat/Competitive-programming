import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

# breakdown:
# window 3 ki 
#

def solve():

    s = input().strip()
    s = list(s)
    count = 0

    for i in range(1 , len(s)-1 ):
        if s[i] == s[i+1] == "u":
            s[i+1] = "s"
            count +=1 
    x1 = s[0]
    x2 = s[-1]
    if x1 == "u":
        count +=1 
    
    if x2 == "u":
        count +=1

    print(count)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()