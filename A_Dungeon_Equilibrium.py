t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    freq = {}

    for num in a:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1

    diff = 0 

    for k , v in freq.items():
        if k == 0:
            diff += v
        elif k == v :
            continue
        elif v>k:
            diff += v-k
        else:
            diff += v

    print(diff)
