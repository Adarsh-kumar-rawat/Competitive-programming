from math import gcd

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

D = Y - X
g = gcd(X, D)
m = D // g

r = A[0] % m
for a in A:
    if a % m != r:
        print(-1)
        exit()

base = []
for a in A:
    base.append((A[0] - a) * X // D)

t_min = -10**30
t_max =  10**30

for i in range(N):
    t_min = max(t_min, -base[i])
    t_max = min(t_max, A[i] - base[i])

if t_min > t_max:
    print(-1)
    exit()


ans = sum(base) + N * t_max
print(ans)
