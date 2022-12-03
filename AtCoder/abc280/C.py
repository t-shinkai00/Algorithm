S = input()
T = input()

for i in range(len(S)):
  if i == len(S)-1:
    if S[i] != T[i]:
      print(len(S))
    else:
      print(len(T))
  if S[i] != T[i]:
    print(i+1)
    break
