t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    left = []
    right = a[:]

    ok = True
    for _ in range(len(a)):
        left.append(right.pop(0))
        if not right:
            break
        if min(left) > max(right):
            print("No")
            ok = False
            break
    
    if ok:
        print("Yes")
