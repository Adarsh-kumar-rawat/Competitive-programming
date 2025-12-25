t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()

    s = ""

    for ch in a:        
        op1 = ch + s
        op2 = s + ch
        s = min(op1, op2)

    print(s)
