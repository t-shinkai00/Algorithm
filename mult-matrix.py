# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_D
n,m,l=map(int,input().split())
tableA=[]
tableB=[]
for i in range(n):
    tableA.append(list(map(int,input().split())))
for i in range(m):
    tableB.append(list(map(int,input().split())))
ans=[[0]*l for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            ans[i][j]+=tableA[i][k]*tableB[k][j]
for i in range(n):
    print(*ans[i])