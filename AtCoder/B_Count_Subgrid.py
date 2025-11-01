N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
patterns = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        block = tuple(S[r][j:j+M] for r in range(i, i + M))
        patterns.add(block)
print(len(patterns))
