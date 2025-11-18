s = input()
u = 0
l = 0 

for ch in s:
    if ch.isupper():
        u +=1
    else:
        l +=1

if u>l:
    print(s.upper())
else:
    print(s.lower())