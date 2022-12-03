# https://atcoder.jp/contests/abc280/tasks/abc280_a
H, W = map(int, input().split())
cnt = 0
for _ in range(H):
  for el in input():
    if el == "#":
      cnt += 1
print(cnt)