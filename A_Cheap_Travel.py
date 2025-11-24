n , m , a , b = map(int,input().split())

a_min = n*a 
cost = 0 
val = n//m + 1
m_min = val*b

special = (n//m)*b + (n%m)*a

print(min(special,a_min,m_min))

