n, m = map(int, input().split())
a = list(map(int, input().split()))

start_i=0
printed = 0
while printed < n or start_i < m:
  # print((printed, start_i))
  if start_i == m:
    for k in range(printed+1, n+1):
      print(k, end=" ")
    printed = n
    break
  if printed < a[start_i]:
    for k in range(printed+1, a[start_i]):
      print(k, end=" ")
    printed = a[start_i]-1
  end_i = start_i
  while end_i < m - 1 and a[end_i+1] - a[end_i] == 1: end_i += 1
  if start_i == end_i:
    # print((a[start_i],a[start_i]+1))
    print(a[start_i]+1, a[start_i], end=" ")
    printed = a[start_i]+1
    start_i += 1
  else:
    # print((a[start_i],a[end_i]+1))
    for k in range(a[end_i]+1, a[start_i]-1, -1):
      print(k, end=" ")
    printed = a[end_i]+1
    start_i = end_i + 1
print()