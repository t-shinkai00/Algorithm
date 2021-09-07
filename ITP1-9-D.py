# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_D
string=list(input())
n=int(input())
for i in range(n):
    command=list(map(str,input().split()))
    a=int(command[1])
    b=int(command[2])+1
    if len(command)==4:
        to=command[3]
    if command[0]=="print":
        print(*string[a:b],sep="")
    elif command[0]=="replace":
        string[a:b]=to
    elif command[0]=="reverse":
        string[a:b]=reversed(string[a:b])
    # print(*string,sep="")