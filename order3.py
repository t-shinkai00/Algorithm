list=list(map(int,input().split()))
for i in range(len(list)):
    for j in range(i,0,-1):
        if list[j-1]>list[j]:
            list[j-1],list[j]=list[j],list[j-1]
print(list[0],list[1],list[2])