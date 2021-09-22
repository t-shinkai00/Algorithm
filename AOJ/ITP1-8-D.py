# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_D
s=input()
p=input()
ans="No"
for i in range(len(s)):
    for j in range(len(p)):
        if s[(i+j)%len(s)]!=p[j]:
            break
    if j==len(p)-1 and s[(i+j)%len(s)]==p[j]:
        ans="Yes"
        break
print(ans)