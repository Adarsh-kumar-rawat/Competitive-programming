n , h = map(int , input().split())
a = list(map(int , input().split()))

count = 0
for num in a :
    if num> h:
        count +=1
    else:
        continue

print(((len(a)-count)+count*2))