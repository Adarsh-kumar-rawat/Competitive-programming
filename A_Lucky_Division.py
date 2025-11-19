n = int(input())

lucky = [4,7,47,74,444,777,447,474,747,774,44,77,477]

for num in lucky:
    if n%num == 0 :
        print("YES")
        break
    else:
        continue
else:
    print("NO")