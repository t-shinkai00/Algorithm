n = int(input())

A = sorted(list(map(int, input().split())))
# print(A)

count = 0
for i in range(n):
  for j in range(n):
    if A[j] > A[i]:
      break
    for k in range(j+1):
      # print(i, j, k)
      if A[i] == A[j] * A[k]:
        if j != k:
          count += 2
        else:
          count += 1
        # print(f"{i}, {j}, {k}, {A[i]} = {A[j]} * {A[k]}")
      elif A[i] < A[j] * A[k]:
        break

print(count)