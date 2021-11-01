# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_B
def selection_sort(arr,N):
  global count
  for i in range(N):
    index=i
    for j in range(i,N):
      if arr[j]<arr[index]:
        index=j
    if index>i:
      arr[i],arr[index]=arr[index],arr[i]
      count+=1
      # print(i,j,arr)

N=int(input())
A=list(map(int,input().split()))
count=0
selection_sort(A,N)
print(*A)
print(count)