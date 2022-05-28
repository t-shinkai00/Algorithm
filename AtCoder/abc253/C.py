from collections import defaultdict

Q = int(input())
S = defaultdict(int)

maxv = 0
minv = 10**10

for _ in range(Q):
  q = list(map(int, input().split()))

  if q[0] == 1:
    S[q[1]] += 1
    maxv = max(maxv, q[1])
    minv = min(minv, q[1])

  elif q[0] == 2:
    S[q[1]] -= min(S[q[1]], q[2])

    if S[q[1]] == 0:
      del S[q[1]]

      if len(S) > 0:
        if q[1] == maxv:
          maxv = max(S)
        if q[1] == minv:
          minv = min(S)
      else:
        maxv = 0
        minv = 10**10

  elif q[0] == 3:
    print(maxv - minv)