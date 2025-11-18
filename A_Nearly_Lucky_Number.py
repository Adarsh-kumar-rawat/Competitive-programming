n = int(input())
s = str(n)
count = 0

for ch in s:
    if ch =='7' or ch == '4':
        count +=1
    else:
        continue

print("YES") if count == 7 or count == 4 else print("NO")