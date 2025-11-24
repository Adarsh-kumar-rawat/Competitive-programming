s = input()

for ch in s:
    if ch == 'H' or ch == "Q" or ch == "9":
        print("YES")
        break
    else:
        continue
else:
    print("NO")