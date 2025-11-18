s = input()
lis = list(s)
count = 0 
for i in range(1,len(lis)):
    if lis[i] == lis[i-1]:
        count +=1
        if count >=6:
            print("YES")
            break
    else:
        count = 0 
else:
    print("NO")