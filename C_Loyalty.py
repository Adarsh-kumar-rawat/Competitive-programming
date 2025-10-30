def solve():
    t = int(input())
    for _ in range(t):
        n, X = map(int, input().split())
        prices = list(map(int, input().split()))
        
        sorted_prices = sorted(prices)
        
        order = []
        left = 0
        right = n - 1
        S = 0
        
        while left <= right:
            current_level = S // X
            next_threshold = (current_level + 1) * X
            gap = next_threshold - S
            
            if sorted_prices[right] >= gap:
                order.append(sorted_prices[right])
                S += sorted_prices[right]
                right -= 1
            else:
                order.append(sorted_prices[left])
                S += sorted_prices[left]
                left += 1
        total_bonus = 0
        S = 0
        for p in order:
            old_level = S // X
            S += p
            new_level = S // X
            if new_level > old_level:
                total_bonus += p
        
        print(total_bonus)
        print(' '.join(map(str, order)))

solve()