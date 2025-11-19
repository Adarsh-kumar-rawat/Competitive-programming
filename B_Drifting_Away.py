t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    i = 0
    j = 1
    bad = False

    while j < n:
        if (s[i] == '>' and s[j] == '<') or \
           (s[i] == '>' and s[j] == '*') or \
           (s[i] == '*' and s[j] == '<'):
            print(-1)
            bad = True
            break
        else:
            i += 1
            j += 1

    if bad:
        continue  

    c1 = 0
    c2 = 0
    c3 = 0

    for ch in s:
        if ch == '<':
            c1 += 1
        elif ch == '>':
            c3 += 1
        else:
            c2 += 1

    if c2 >= 2:
        print(-1)
    else:
        print(max(c1 + c2, c2 + c3))
