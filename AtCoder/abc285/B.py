N = int(input())
S = input()

for i in range(1, N):
  for l in range(N-i):
    if S[l] == S[l+i]:
      l -= 1
      break
  print(l+1)