n = int(input())
prev = input().strip()
count = 1
for _ in range(n - 1):
    curr = input().strip()
    if curr != prev:
        count += 1
    prev = curr
print(count)
