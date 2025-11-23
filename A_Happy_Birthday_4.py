x , y , z = map(int,input().split())

if y>x:
    print("No")
elif x < y*z:
    print("No")
elif (x-y*z)%(z-1) != 0:
    print("No")
else:
    print("Yes")