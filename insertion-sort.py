# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A
def insertionSort(A,N):
    for i in range(1,N):
        for j in range(len(A)):
            if j==len(A)-1:
                print(A[j])
            else:
                print(A[j],end=" ")
        v=A[i]
        j=i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j-=1
        A[j+1]=v
N=int(input())
A=list(map(int,input().split()))
insertionSort(A,N)
for j in range(len(A)):
    if j==len(A)-1:
        print(A[j])
    else:
        print(A[j],end=" ")