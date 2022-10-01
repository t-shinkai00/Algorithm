n, q = map(int, input().split())
a = []
for _ in range(n):
  input_ = list(map(int, input().split()))
  l = input_.pop(0)
  a.append(input_)

# print("----------------")
# print(a)
for _ in range(q):
  s, t = map(int, input().split())
  print(a[s-1][t-1])