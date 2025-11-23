N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
diff = total - M 

if diff in A:
    print("Yes")
else:
    print("No")