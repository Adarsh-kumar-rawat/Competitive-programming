N, M, K  = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

rob = 0 
# agar h ka 1st is bigger than b ka first than
#  h = [2,3,4,5,] b = [1,4,5,]

i = j = rob = 0

while i < N and j < M:
    if H[i] <= B[j]:
        rob += 1
        i += 1
        j += 1
    else:
        j += 1

print("Yes" if rob >= K else "No")