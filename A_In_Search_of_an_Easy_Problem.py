n = int(input())
nums = list(map(int , input().split()))

for num in nums:
    if num == 1:
        print("HARD")
        break
    else:
        continue
else:
    print("EASY")