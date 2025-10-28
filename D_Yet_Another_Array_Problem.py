import sys

def main():
    input = sys.stdin.readline
    Prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = None
        for num in a:
            for x in Prime:
                if num % x != 0:
                    if ans is None or x < ans:
                        ans = x
                    break
        if ans is None:
            ans = -1
        print(ans)

if __name__ == "__main__":
    main()
