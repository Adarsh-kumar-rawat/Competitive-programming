import sys
input = sys.stdin.readline

from collections import defaultdict, Counter, deque
import math
import bisect

INF = 10**18
MOD = 10**9 + 7

"""
agar y is in the list than y +=1 
agar range ki oi value list mei nahi than ans is 
x + y-1 

gar hai to jitnin values hai , less say 5 , than the ans will be y + 5 

sort the arr firstt 
bisect serch to find idx and compute 

arr = [10,11,12,13]

14 ,15 , 16 ,17 -> 17 

x = 10 , y = 4 
l = 10 
r = 18 
mid = 14 
idx 4th 

count= 4 
miss = 14 - 10 - 4 = 0 

l = 14 , r = 18 , mid = 32//2 = 16 
4th 
,iss = 16 - 10 +1 - 4 = 3
l = 16 
r = 18 
mid = 17 
count  4 
17 - 10 +1  - 4 =  4 
"""
def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort() 
    res = []

    for _ in range(q):
        x, y = map(int, input().split())
        
        idx = bisect.bisect_left(arr, x)
        relevant = arr[idx:]

        left = x
        right = x + y + len(relevant)
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            count = bisect.bisect_right(relevant, mid)
            missing = mid - x + 1 - count 
            
            if missing >= y:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        res.append(ans)

    for num in res:
        print(num)

def main():
    t = 1 
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()