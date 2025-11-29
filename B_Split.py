t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = 0 
    freq = {}
    p = [0]*n
    q = [0]*n
    for num in a:
        if num in freq:
            freq[num] += 1 
        else:
            freq[num] = 1 
    
    print(freq)

    for val in freq.values():
        if val == 1:
            count += 1 
        else:
            x = val//2
