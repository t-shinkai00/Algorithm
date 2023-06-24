def is_kaibun(s):
    if str(s) == str(s)[::-1]:
        return True
    else: return False


n=int(input())
S=[]
for _ in range(n):
    S.append(input())

flag = False

for i in range(n):
    for j in range(i+1,n):
        if is_kaibun(S[i]+S[j]) or is_kaibun(S[j]+S[i]):
            flag = True

if flag: print("Yes")
else: print("No")