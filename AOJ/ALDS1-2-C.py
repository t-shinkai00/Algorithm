# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_C
def bubble_sort(arr,N):
  flag=True
  while flag:
    flag=False
    for j in range(N-1,0,-1):
      # print(j,arr)
      if int(arr[j][1])<int(arr[j-1][1]):
        arr[j], arr[j-1]=arr[j-1], arr[j]
        flag=True

def selection_sort(arr,N):
  for i in range(N):
    index=i
    for j in range(i,N):
      if int(arr[j][1])<int(arr[index][1]):
        index=j
    if index>i:
      arr[i],arr[index]=arr[index],arr[i]
      # print(i,j,arr)

N=int(input())
cardsA=list(map(str,input().split()))
cardsB=cardsA.copy()
bubble_sort(cardsA,N)
selection_sort(cardsB,N)
print(*cardsA)
print("Stable")
print(*cardsB)
print("Stable" if cardsA==cardsB else "Not stable")