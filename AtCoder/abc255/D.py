import itertools
import bisect


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)
B=list(itertools.accumulate(A))
# print(B)
for _ in range(Q):
  target = int(input())
  i=bisect.bisect(A,target)
  # print(target, i)
  if i==0 or i==N:
    print(abs(B[N-1]-target*N))
  else:
    print(target*2*i-2*B[i-1]+B[N-1]-target*N)