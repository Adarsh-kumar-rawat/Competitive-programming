n = int(input())
m = list(map(int,input().split()))

m.sort(reverse= True)
my = 0
t = sum(m)
i = 0
count = 0
while my <= t - my:
    my += m[i]
    count +=1
    i +=1
print(count)