import math
N, M = map(int, input().split())

def meet_num(n, m):
  if m > n**2: return -1
  elif math.sqrt(m) <= n or m < n: return m
  else:
    i = m
    while True:
      s = math.floor(math.sqrt(i))
      t = i/s
      if t.is_integer() and t <= n:
        return i
      s += 1
      if t.is_integer() and t <= n:
        return i
      i += 1

print(meet_num(N,M))