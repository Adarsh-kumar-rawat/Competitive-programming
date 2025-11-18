n = int(input())

# number of evens
ne = n // 2
sum_even = ne * (ne + 1)

# number of odds
no = (n + 1) // 2
last_odd = 2 * no - 1
sum_odd = no * (1 + last_odd) // 2

print(sum_even - sum_odd)
