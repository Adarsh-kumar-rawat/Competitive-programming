import sys
input = sys.stdin.readline
 
from collections import defaultdict, Counter, deque
import math
import bisect
 
INF = 10**18
MOD = 10**9 + 7
 
"""
valid pairs 
00000
11111
1followed by zeroes 
so basically until we have 1 folled by some zeroes we can make move 
10 in str 
 
if at any point s become 1111 or 0000 we cant make any valid moves 
so ifthe move is 0 bob wins move is 1 alice wins , ig move mod 2 is even bob wins 
else alice wins 
 
we need to find 10 pairs 
any pair wich is like 11100
so 2 zero and 3 one we can than replace it with 00111
than the other person won't be able to move 
000101010010
here 4 moves are possible 
so we just need to make sure that after a 1 it is follwed by zeros and if we find another 1 we try to find another cons 0 fopr that 
"""

def solve():
    n = int(input())
    s = input().strip()
    i = 0
    idx = []

    while i < n:

        if s[i] == '0':
            i += 1
            continue

        start = i

        while i < n and s[i] == '1':
            i += 1
        
        if i < n and s[i] == '0':
            while i < n and s[i] == '0':
                i += 1
            end = i - 1
            idx.append((start + 1, end + 1))

    count = len(idx)
    total = 0 

    for i in range(len(idx)):
        a , b = idx[i]
        m = b - a +1 
        total += m//2

    if total % 2 == 0:
        print("Bob")
    else:
        print("Alice")
        first, last = idx[-1]
        m = last - first + 1
        indices = list(range(first, last + 1))
        print(m)
        print(*indices)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
