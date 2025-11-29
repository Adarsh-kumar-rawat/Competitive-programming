s = input()
res = list(s)

for i in range(len(res)):
    d = int(res[i])
    flip = 9 - d

    if i == 0 and d == 9:
        continue 

    if flip < d:
        res[i] = str(flip)

print("".join(res))
