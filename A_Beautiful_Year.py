n = int(input())

def check(num):
    s = str(num)
    if len(s) == len(set(s)):
        return num
v = n+1
while True:
    if check(v):
        print(v)
        break
    v += 1
