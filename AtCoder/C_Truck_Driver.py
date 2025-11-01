N, A, B = map(int, input().split())
S = input().strip()

prefix_a = [0] * (N + 1)
prefix_b = [0] * (N + 1)

for i in range(N):
    prefix_a[i + 1] = prefix_a[i] + (S[i] == 'a')
    prefix_b[i + 1] = prefix_b[i] + (S[i] == 'b')

ans = 0
l_a = l_b = 0

for i in range(1, N + 1):
    while prefix_b[i] - prefix_b[l_b] >= B:
        l_b += 1

    while l_a < i and prefix_a[i] - prefix_a[l_a] >= A:
        l_a += 1
    ans += max(0, l_a - l_b)

print(ans)
