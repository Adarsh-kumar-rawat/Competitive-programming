t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    even_count = 0
    odd_count = 0

    for x in a:
        if x % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if even_count > 0 and odd_count > 0:
        a.sort()

    print(*a)
