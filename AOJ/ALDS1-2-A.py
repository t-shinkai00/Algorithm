# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A
def bubble_sort(arr,N):
  global count
  flag=True
  while flag:
    flag=False
    for j in range(N-1,0,-1):
      # print(j,arr)
      if arr[j]<arr[j-1]:
        arr[j], arr[j-1]=arr[j-1], arr[j]
        count+=1
        flag=True

N=int(input())
A=list(map(int,input().split()))
count=0
bubble_sort(A,N)
print(*A)
print(count)