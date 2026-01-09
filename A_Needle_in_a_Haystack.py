import sys
from collections import Counter

input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()

    ct = Counter(t)
    cs = Counter(s)

    for c in cs:
        if cs[c] > ct[c]:
            print("IMPOSSIBLE")
            return

    for c in s:
        ct[c] -= 1

    less = []
    equal = []
    greater = []

    for c in sorted(ct):
        if c < s[0]:
            less.append(c * ct[c])
        elif c == s[0]:
            equal.append(c * ct[c])
        else:
            greater.append(c * ct[c])

    option1 = "".join(less) + s + "".join(equal) + "".join(greater)
    option2 = "".join(less) + "".join(equal) + s + "".join(greater)

    print(min(option1, option2))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
