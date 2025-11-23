import sys
data = sys.stdin.read().split()
t = int(data[0])
idx = 1
out = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    s = data[idx]; idx += 1
    queries = list(map(int, data[idx:idx + q])); idx += q

    if 'B' not in s:
        for a in queries:
            out.append(str(a))
        continue

    for a in queries:
        pos = 0
        sec = 0
        while a > 0:
            if s[pos] == 'A':
                a -= 1
            else:
                a //= 2
            sec += 1
            pos += 1
            if pos == n:
                pos = 0
        out.append(str(sec))

sys.stdout.write("\n".join(out))
