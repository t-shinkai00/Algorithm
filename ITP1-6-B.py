# https://onlinejudge.u-aizu.ac.jp/solutions/problem/ITP1_6_B
list=[]
for i in range(4*3*10):
    list.append(0)
n=int(input())
for i in range(n):
    b,f,r,v=map(int,input().split())
    list[(b-1)*3*10+(f-1)*10+r-1]+=v
for b in range(4):
    for f in range(3):
        for r in range(10):
            print(f" {list[b*3*10+f*10+r]}",end="")
        print()
    if b<3:
        print("####################")