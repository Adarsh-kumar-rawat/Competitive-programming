import sys
from collections import deque

input = sys.stdin.readline
INF = 10**18


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort()

    dist = [INF] * (n + 1)
    q = deque()

    for num in arr:
        if num <= n:
            dist[num] = 1
            q.append(num)

    while q:
        x = q.popleft()

        for num in arr:
            nx = x * num
            if nx > n:
                break   

            if dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                q.append(nx)

    print(*(-1 if dist[i] == INF else dist[i] for i in range(1, n + 1)))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
