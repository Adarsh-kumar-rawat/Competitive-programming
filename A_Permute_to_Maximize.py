a,b,c = map(int, input().split())

nums = sorted([a, b, c]) 

x = nums[2]*100
y = nums[1]*10
z = nums[0]

print(x+y+z)