# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_B
while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    else:
        count=0
        for i in range(1,n+1):
            for j in range(1,i):
                for k in range(1,j):
                    if i==j or j==k or k==i:
                        break
                    if i+j+k==x:
                        count+=1
                        break
        print(count)