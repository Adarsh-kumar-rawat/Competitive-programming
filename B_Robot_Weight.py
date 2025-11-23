X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
P = [int(input()) for _ in range(Q)]

curr = X

freq = set()

for p in P:
    if p in freq:
        curr -= W[p-1]
        freq.remove(p)
    else:
        curr += W[p-1]
        freq.add(p)
    print(curr)


