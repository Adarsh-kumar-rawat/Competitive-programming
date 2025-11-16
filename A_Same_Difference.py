t = int(input())

for _ in range(t):
    n = int(input())
    s = (input())
    nums = list(s)
    count = 0 

    x = nums[-1]
    for ch in s:
        if ch != x:
            count +=1
    print(count)