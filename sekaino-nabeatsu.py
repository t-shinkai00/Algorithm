x=int(input())
for i in range(1,x+1):
    if i%3==0:
        print(f" {i}",end="")
    else:
        n=i
        while n>0:
            if n%10==3:
                print(f" {i}",end="")
                break
            n//=10