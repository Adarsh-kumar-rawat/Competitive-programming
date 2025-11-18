s = input().strip()
target = "hello"
j = 0

for ch in s:
    if ch == target[j]:
        j += 1
        if j == len(target):
            break

print("YES" if j == len(target) else "NO")
