import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7


def solve():
    """
    breakdown:
    """

    n = int(input())
    arr = list(map(int, input().split()))

    new = arr.copy()
    new.sort(reverse = True)

    if arr == new:
        print(*arr)
        return 
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[arr[i]] = i

    left = 0
    candidate = n

    while left < n:
        if pos[candidate] == left:
            left += 1
            candidate -= 1
        else:
            r = pos[candidate]
            arr[left:r+1] = reversed(arr[left:r+1])
            break

    print(*arr)

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()