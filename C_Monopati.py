'''

You are given a grid a of 2 rows and n columns, where every cell has value from 1 to 2n

.

Let f(l,r)
, where 1≤l≤r≤2n, represent a binary∗ grid b of 2 rows and n columns, such that bi,j=1 if and only if l≤ai,j≤r. Note that cell (i,j) denotes the cell i rows from the top and j

columns from the left.

Count the number of pairs of integers (l,r)
such that 1≤l≤r≤2n, and in f(l,r) there exists a down-right path of adjacent cells† with value of 1 from cell (1,1) to (2,n)

.

∗
A grid is considered binary if and only if every cell of it has value of 0 or 1

.

†

A down-right path of adjacent cells is a sequence of cells such that each cell in the sequence shares either its top side or its left side with a side of the previous cell in the sequence.
Input

Each test contains multiple test cases. The first line contains the number of test cases t
(1≤t≤104

). The description of the test cases follows.

The first line of each test case contains a single integer n
(2≤n≤2⋅105

) — the number of columns in the grid.

The second line contains exactly n
integers a1,1, a1,2, ..., a1,n (1≤a1,i≤2n

) — the values of the cells of the first row of the grid.

The third line contains exactly n
integers a2,1, a2,2, ..., a2,n (1≤a2,i≤2n

) — the values of the cells of the second row of the grid.

It is guaranteed that the sum of n
across all test cases does not exceed 2⋅105

.
Output

For every test case, output on a separate line a single integer representing the number of pairs of integers (l,r)
such that 1≤l≤r≤2n, and in f(l,r) there exists a down-right path of adjacent cells with value of 1 from cell (1,1) to (2,n)

'''

import sys

def solve():
    n = int(sys.stdin.readline())
    top = list(map(int, sys.stdin.readline().split()))
    bottom = list(map(int, sys.stdin.readline().split()))
    
    total = 2 * n  # values go from 1 to 2n
    
    # prefix min/max for top row
    top_min = [0] * n
    top_max = [0] * n
    
    # suffix min/max for bottom row
    bottom_min = [0] * n
    bottom_max = [0] * n
    
    top_min[0] = top_max[0] = top[0]
    for i in range(1, n):
        top_min[i] = min(top_min[i - 1], top[i])
        top_max[i] = max(top_max[i - 1], top[i])
    
    bottom_min[-1] = bottom_max[-1] = bottom[-1]
    for i in range(n - 2, -1, -1):
        bottom_min[i] = min(bottom_min[i + 1], bottom[i])
        bottom_max[i] = max(bottom_max[i + 1], bottom[i])
    
    # store right limits for each left value
    right_for_left = [[] for _ in range(total + 2)]
    
    start_val = top[0]
    end_val = bottom[-1]
    
    for j in range(n):
        min_here = min(top_min[j], bottom_min[j])
        max_here = max(top_max[j], bottom_max[j])
        
        left_val = min(min_here, start_val)
        right_val = max(max_here, end_val)
        
        right_for_left[left_val].append(right_val)
    
    ans = 0
    smallest_right = total + 1
    
    for left in range(total, 0, -1):
        for right in right_for_left[left]:
            smallest_right = min(smallest_right, right)
        
        limit = max(left, smallest_right)
        if limit <= total:
            ans += (total - limit + 1)
    
    print(ans)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
