A=[11,10,11,11,7,11,11,3,8]
i=0
def read_log():
  global A,i
  if i>=len(A):
    return -1
  else:
    result=A[i]
    i+=1
    return result

element=None
cnt=0
u=read_log()
while u != -1:
  if cnt==0:
    cnt+=1
    element=u
  else:
    if element==u:
      cnt+=1
    else:
      cnt-=1
      if cnt==0:
        element=None
  u=read_log()
print(element,cnt)