# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D
n=int(input())
minv=int(input())
maxv=-10**12
for i in range(n-1):
    r=int(input())
    maxv=max(maxv,r-minv)
    minv=min(minv,r)
print(maxv)