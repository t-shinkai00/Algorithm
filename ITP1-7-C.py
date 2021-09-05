# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/7/ITP1_7_C
r,c=map(int,input().split())
table=[]
for i in range(r):
    sum=0
    line=list(map(int,input().split()))
    for j in range(c):
        sum+=line[j]
    line.append(sum)
    table.append(line)
line=[]
for j in range(c+1):
    sum=0
    for i in range(r):
        sum+=table[i][j]
    line.append(sum)
table.append(line)
for i in range(r+1):
    print(*table[i])