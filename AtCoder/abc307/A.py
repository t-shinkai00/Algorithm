n = int(input())
a = list(map(int, input().split()))

# https://atcoder.jp/contests/abc307/tasks/abc307_a
ans=[]
for i in range(n):
    ans.append(str(sum(a[7*i:7*(i+1)])))
print(" ".join(ans))