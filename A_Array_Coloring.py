import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
sorted order yani odd even , to odd pe R and even pe B daal do 
"""
def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    res = []
    for i in range(n):
        num = arr[i]
        if num % 2 == 0:
            res.append(0)
        else:
            res.append(1)

    flag = True

    for i in range(1,n):
        curr = res[i]
        prev = res[i-1]

        if curr == prev:
            print("NO")
            flag = False
            break

    if flag:
        print("YES")


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()