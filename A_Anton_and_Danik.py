n = int(input())
s = input().strip()

a = 0
d = 0

for ch in s:
    if ch == "A":
        a += 1
    elif ch == "D":
        d += 1

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")
