N = int(input())
S = list(map(int, input().split()))

summary = 0
for el in S:
  print(el-summary, end=" ")
  summary = el
print()