def search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0  # index for pattern
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1  # found index
    return -1


T = int(input().strip())

for _ in range(T):
    A = input().strip()
    B = input().strip()
    n = len(A)

    if A.count('1') != B.count('1'):
        print(-1)
        continue

    AA = A + A
    idx = search(AA, B)

    if idx == -1 or idx >= n:
        print(-1)
    else:
        print(idx)
