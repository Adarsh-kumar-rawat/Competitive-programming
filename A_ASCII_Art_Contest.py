z = list(map(int, input().split()))
a = max(z)
b = min(z)
z.sort()
if a - b >=10:
    print("check again")
else:
    print("final",z[1])