t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    new_a = []
    new_b = []

    for i in range(0,len(a),2):
        if a[i] < b[i]:
            temp = a[i]
            a[i] = b[i]
            b[i] = temp
    for i in range(1,len(a),2):
        if b[i] < a[i]:
            temp = b[i]
            b[i] = a[i]
            a[i] = temp
    xor_1 = 0
    for n in a:
        xor_1 ^= n

    xor_2 = 0
    for n in b:
        xor_2 ^= n

    if xor_1>xor_2:
        print("Ajisai")
    elif xor_2 > xor_1:
        print("Mai")
    else:
        print("Tie")