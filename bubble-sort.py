def bubble_sort(arr):
    N=len(arr)
    for i in range(N):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                print(i,j,arr)

arr=list(map(int,input().split()))
bubble_sort(arr)
print(arr)