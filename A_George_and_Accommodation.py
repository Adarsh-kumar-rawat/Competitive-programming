n = int(input())
rooms = []
for _ in range(n):
    p, q = map(int, input().split())
    rooms.append((q - p))
count = 0 
for num in rooms:
    if num >= 2:
        count +=1
print(count)