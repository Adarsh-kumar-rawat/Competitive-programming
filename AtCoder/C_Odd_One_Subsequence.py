from collections import Counter

N = int(input())
A = list(map(int, input().split()))

freq = Counter(A)
ans = 0
for f in freq.values():
    ans += (f * (f - 1) // 2) * (N - f)

print(ans)
