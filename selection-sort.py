def selection_sort(arr):
  N=len(arr)
  for i in range(N):
    index=i
    for j in range(i,N):
      if arr[j]<arr[index]:
        index=j
    if index>i:
      arr[i],arr[index]=arr[index],arr[i]
      print(i,index,arr)

A=list(map(int,input().split()))
selection_sort(A)
print(*A)