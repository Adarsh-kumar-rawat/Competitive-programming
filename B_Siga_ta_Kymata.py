'''
You are given a permutation∗ p of every integer from 1 to n. You also own a binary† string s of size n where si=0 for all 1≤i≤n. You may do the following operation at most 5

times:

    Choose any two integers l

and r such that 1≤l≤r≤n. Then, for every i such that l<i<r and min(pl,pr)<pi<max(pl,pr) hold at the same time, you will set si to 1

    . 

You are also given a binary string x
of size n. After performing operations, it must hold for every 1≤i≤n that if xi=1, then si=1. Note that if xi=0, then si

can have any value.

Figure out any sequence of at most 5

operations such that the aforementioned condition is satisfied, or report that it is impossible to do so. Note that you do not have to minimize the number of operations you make.

∗
A permutation p of every integer from 1 to n is a sequence of elements from 1 to n

such that every element appears exactly once.

†
A string b of size m is considered binary if and only if bi=0 or bi=1 for all 1≤i≤m

.
Input

Each test contains multiple test cases. The first line contains the number of test cases t
(1≤t≤104

). The description of the test cases follows.

The first line of each test case contains a single integer n
(3≤n≤2⋅105

) — the size of the array.

The second line contains exactly n
integers p1,p2,…,pn (1≤pi≤n, the elements of p are pairwise distinct) — where pi is the i

-th element of the permutation.

The third line contains a single binary string x
of size n

.

It is guaranteed that the sum of n
over all test cases does not exceed 2⋅105

.
Output

For each test case, if it is impossible to perform operations such that the constraint is satisfied, output −1

.

Otherwise, output an integer 0≤k≤5
, the number of operations. On the i-th of the next k lines, output two integers 1≤li≤ri≤n, the bounds of the i-th operation that is performed. If there are multiple correct solutions, output any of them
'''

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        x = input().strip()
        
        targets = [i for i in range(n) if x[i] == '1']
        
        if not targets:
            print(0)
            continue
        
        operations = []
        covered = [False] * n
        
        for target in targets:
            if covered[target]:
                continue
            
            found = False
            
            
            for l in range(n):
                for r in range(l + 2, n):  
                    if l < target < r:
                        min_val = min(p[l], p[r])
                        max_val = max(p[l], p[r])
                        
                        if min_val < p[target] < max_val:
                            operations.append((l + 1, r + 1))  
                            
                            
                            for i in range(l + 1, r):
                                if min_val < p[i] < max_val:
                                    covered[i] = True
                            
                            found = True
                            break
                
                if found:
                    break
            
            if not found:
                print(-1)
                break
        else:
            all_covered = all(covered[i] for i in targets)
            
            if all_covered and len(operations) <= 5:
                print(len(operations))
                for l, r in operations:
                    print(l, r)
            else:
                print(-1)

solve()