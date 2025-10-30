import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        R0 = int(next(it)); X = int(next(it)); D = int(next(it)); n = int(next(it))
        s = next(it).strip()
        L = R = R0
        ans = 0
        for c in s:
            if c == '1':
                ans += 1
                L = max(0, L - D)
                R = R + D
            else: 
                if R < X:
                    ans += 1
                    L = max(0, L - D)
                    R = R + D
                elif L >= X:
                    pass
                else:
                    ans += 1
                    L = max(0, X - 1 - D)
                    R = X - 1 + D
        out_lines.append(str(ans))
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
