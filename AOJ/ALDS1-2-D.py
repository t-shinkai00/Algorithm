# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D
def insertionSort(arr, n, g):
  global count
  for i in range(g, n):
    v=arr[i]
    j=i-g
    while j>=0 and arr[j]>v:
      arr[j+g]=arr[j]
      j=j-g
      count+=1
    arr[j+g]=v

n=int(input())
A=[int(input()) for i in range(n)]
count = 0
G=[1]
for i in range(n):
  x=3*G[-1]+1
  if n<x:
    break
  G.append(x)
m=len(G)
G.reverse()
for i in range(m):
  insertionSort(A, n, G[i])

print(m)
print(*G)
print(count)
print(*A, sep="\n")