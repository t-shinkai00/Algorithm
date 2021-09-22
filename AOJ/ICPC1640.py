# https://onlinejudge.u-aizu.ac.jp/challenges/sources/ICPC/Prelim/1640
while True:
    n=int(input())
    if n==0:
        break
    d=list(map(int,input().split()))
    count=0
    for i in range(n-3):
        if d[i]==2 and d[i+1]==0 and d[i+2]==2 and d[i+3]==0:
            count+=1
    print(count)