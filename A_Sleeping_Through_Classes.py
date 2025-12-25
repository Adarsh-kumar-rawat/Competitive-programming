t = int(input())

for _ in range(t):

    n, k = map(int, input().split())
    s = input()

    count = 0
    i = 0

    while i < n:
        if s[i] == '1':
            i += k + 1  
        else:
            count += 1  
            i += 1

    print(count)
