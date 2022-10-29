# https://atcoder.jp/contests/abc275/tasks/abc275_a
N = int(input())
H = list(map(int, input().split()))

if N == 1:
  print("1")
else:
  maximum = max(H)
  print(H.index(maximum)+1)