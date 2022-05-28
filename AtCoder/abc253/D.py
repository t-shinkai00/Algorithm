import math

def sum(n):
  return (n*(n+1))//2

n, a, b = map(int, input().split())

lcm = a * b // math.gcd(a,b)

a_times = n // a
b_times = n // b
lcm_times = n // lcm

print(sum(n)-a*sum(a_times)-b*sum(b_times)+lcm*sum(lcm_times))