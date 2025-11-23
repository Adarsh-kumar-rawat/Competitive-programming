from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

S = input().strip()
safe = [i for i in range(N) if S[i] == 'S'] # ATLEAST 2 SAFE
dangerous = [i for i in range(N) if S[i] == 'D'] # AT LEAST 1 DANGEROUS

dist = [float('inf')] * N
first_safe = [-1] * N
q = deque()

for s in safe:
    dist[s] = 0
    first_safe[s] = s
    q.append(s)

while q:
    u = q.popleft()
    for v in edges[u]:
        if dist[v] > dist[u] + 1:
            dist[v] = dist[u] + 1
            first_safe[v] = first_safe[u]
            q.append(v)

answers = []

for v in dangerous:
    min_dist = float('inf')
    q = deque()
    visited = [False]*N
    visited[v] = True
    q.append((v, 0))
    while q:
        u, d = q.popleft()
        if S[u] == 'S' and u != first_safe[v]:
            min_dist = d
            break
        for w in edges[u]:
            if not visited[w]:
                visited[w] = True
                q.append((w, d+1))
    answers.append(dist[v] + min_dist)

for ans in answers:
    print(ans)

# THIS IS A TLE SOLUTION