n=int(input())
list=[]
for i in range(13*4):
    list.append(0)
for i in range(n):
    mark,num=input().split()
    num=int(num)
    if mark=="S":
        block=0
    elif mark=="H":
        block=1
    elif mark=="C":
        block=2
    elif mark=="D":
        block=3
    list[block*13+num-1]=1
for i in range(13*4):
    if list[i]==0:
        if i//13==0:
            print(f"S {i%13+1}")
        elif i//13==1:
            print(f"H {i%13+1}")
        elif i//13==2:
            print(f"C {i%13+1}")
        elif i//13==3:
            print(f"D {i%13+1}")