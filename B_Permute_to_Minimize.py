X = input().strip()
s = sorted(X)

if s[0] == '0':
    for i in range(len(s)):
        if s[i] != '0':
            s[0], s[i] = s[i], s[0]
            break

print("".join(s))
