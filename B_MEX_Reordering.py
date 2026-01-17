import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
sort klarke first point pe split karke check karn a hai 
"""
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mex = 0 

    while mex in arr:
        mex += 1 

    def find_mex(i):
        mex_pre = 0 
        mex_suf = 0 

        pre = arr[:i+1]
        suff = arr[i:]
        while mex_pre in pre :
            mex_pre += 1
        
        while mex_suf in suff :
            mex_suf +=1 

        return mex_pre , mex_suf
    
    flag = True
    for i in range(1,n):
        a , b = find_mex(i)
        if a == b:
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