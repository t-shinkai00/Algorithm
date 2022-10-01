N = int(input())
A = set(map(int, input().split()))
# print(A)

l = 0
r = N + 1

while r - l > 1:
  m = (l + r) // 2  # 2分探索
  c = len(set(range(1, m+1))&A)
  if c + (N - c) // 2 >= m:  # 残った本＋(売った本/2)がm以上ならm卷まで読める
    l = m
  else:
    r = m

print(l)