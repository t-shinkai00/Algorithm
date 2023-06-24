n = int(input())
a = list(map(int, input().split()))

ans=[]
for i in range(n):
    ans.append(str(sum(a[7*i:7*(i+1)])))
print(" ".join(ans))