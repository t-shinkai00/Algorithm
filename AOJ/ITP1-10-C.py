# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_C
import math
while True:
    n=int(input())
    if n==0:
        break
    data=list(map(float,input().split()))
    ave=0.0
    for i in range(n):
        ave+=data[i]/n
    a2=0.0
    for i in range(n):
        a2+=(data[i]-ave)**2/n
    print(math.sqrt(a2))