N = int(input())
parts = [tuple(map(int, input().split())) for _ in range(N)]
S = sum(w for w, _, _ in parts)
sumB = sum(b for _, _, b in parts)
gain_items = [(w, h - b) for w, h, b in parts if h - b > 0]
C = S // 2
if C == 0 or not gain_items:
    print(sumB)
else:
    dp = [0] * (C + 1)
    for w, g in gain_items:
        if w > C:
            continue
        for c in range(C, w - 1, -1):
            v = dp[c - w] + g
            if v > dp[c]:
                dp[c] = v
    print(sumB + max(dp))
