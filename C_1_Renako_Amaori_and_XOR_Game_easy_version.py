t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0 
    res = []

    for i in range(len(a)):
        if a[i] != b[i]:
            res.append(i+1)
            count +=1 

    if count%2 == 0:
        print("Tie")
    else:
        if res[-1]%2 ==0:
            print("Mai")
        else:
            print("Ajisai")