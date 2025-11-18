l , b = map(int, input().split())
count = 0 
while l <= b:
    l = 3*l
    b = 2*b
    count +=1
#print(l,b)
print(count)