import sys
data = list(map(int, sys.stdin.read().split()))
N, M, C = data[0], data[1], data[2]
A = data[3:]
A.sort()
Pos = [0]*(2*N)
for i in range(N):
    Pos[i] = A[i]
    Pos[i+N] = A[i]+M
group_end = [0]*(2*N)
i = 0
while i < 2*N:
    j = i
    while j+1 < 2*N and Pos[j+1] == Pos[i]:
        j += 1
    for k in range(i, j+1):
        group_end[k] = j
    i = j+1
total = 0
for u in range(N):
    prev_pos = A[u-1] if u > 0 else A[N-1]-M
    gap = A[u]-prev_pos
    v = u+C-1
    e = group_end[v]
    cnt = e-u+1
    total += gap*cnt
print(total)
