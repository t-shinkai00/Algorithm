n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for el in L:
  if A[el-1] == n or A[el-1]+1 in A:
    continue
  else:
    A[el-1] += 1
print(*A)