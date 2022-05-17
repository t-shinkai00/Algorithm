S = "".join(map(str,sorted(input())))

upper_flag = False
lower_flag = False

if S == str.lower(S):
  print("No")
  exit()
if S == str.upper(S):
  print("No")
  exit()

for i in range(len(S)-1):
  if S[i] == S[i+1]:
    print("No")
    exit()

print("Yes")
