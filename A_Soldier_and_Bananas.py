k , m , w = map(int, input().split())

cost = 0
n = 1
while w:
    cost += k*n
    w -=1
    n+=1
#print(cost)
if cost < m:
    print(0)
else:
    print(cost-m)