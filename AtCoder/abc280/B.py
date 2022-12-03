# https://atcoder.jp/contests/abc280/tasks/abc280_b
N = int(input())
S = list(map(int, input().split()))

summary = 0
for el in S:
  print(el-summary, end=" ")
  summary = el
print()