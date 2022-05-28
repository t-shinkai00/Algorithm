A, B, C, D, E, F, X = map(int, input().split())

takahashi_time = (X // (A+C)) * A
takahashi_remain = X % (A+C)

aoki_time = (X // (D+F)) * D
aoki_remain = X % (D+F)

if takahashi_remain > A:
  takahashi_time += A
else:
  takahashi_time += takahashi_remain

if aoki_remain > D:
  aoki_time += D
else:
  aoki_time += aoki_remain

takahashi_distance = takahashi_time * B
aoki_distance = aoki_time * E

if takahashi_distance > aoki_distance:
  print("Takahashi")
elif takahashi_distance == aoki_distance:
  print("Draw")
else:
  print("Aoki")