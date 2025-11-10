def is_valid_bracket(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


t = int(input())
for _ in range(t):
    s = input().strip()
    k = int(input())
    n = len(s)
    winner = "First"  # default
    
    for i in range(n - k + 1):
        sub = s[i:i+k]
        if is_valid_bracket(sub):
            winner = "Second"
            break
    print(winner)
