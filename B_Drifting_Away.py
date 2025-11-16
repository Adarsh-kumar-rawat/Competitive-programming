t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    flag = ('*' in s)

    if flag:
        if n == 1:
            print(1)
        else:
            print(-1)
    else:
        if s[0] == '>' and s[-1] == '<':
            print(-1)
        else:
            countleft = 0
            while countleft < n and s[countleft] == '<' or s[countleft] =="*":

                countleft += 1

            countright = 0
            while countright < n and s[n - 1 - countright] == '>' or s[countleft] =="*":
                countright += 1

            print(max(countleft, countright))

