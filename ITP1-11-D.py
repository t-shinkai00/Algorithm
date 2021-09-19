# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/11/ITP1_11_D
def roll(i,direction):
    if direction=="N":
        dices[i][0],dices[i][1],dices[i][4],dices[i][5]=dices[i][1],dices[i][5],dices[i][0],dices[i][4]
    elif direction=="S":
        dices[i][0],dices[i][1],dices[i][4],dices[i][5]=dices[i][4],dices[i][0],dices[i][5],dices[i][1]
    elif direction=="E":
        dices[i][0],dices[i][2],dices[i][3],dices[i][5]=dices[i][3],dices[i][0],dices[i][5],dices[i][2]
    elif direction=="W":
        dices[i][0],dices[i][2],dices[i][3],dices[i][5]=dices[i][2],dices[i][5],dices[i][0],dices[i][3]

def command(l,m):
    global flag
    order="NNNNWNNNWNNNENNNENNNWNNN"
    if dices[l]==dices[m]:
            flag=True
    for i in range(len(order)):
        roll(l,order[i])
        if dices[l]==dices[m]:
            # print(l,m)
            flag=True
            break

def print_dice(i):
    print(dices[i])

n=int(input())
dices=[]
num=0
for i in range(n):
    dice=list(map(int,input().split()))
    dices.append(dice)
    num+=i
# print(num)
flag=False
for i in range(n):
    for j in range(i+1,n,1):
        # print(i,j)
        command(i,j)
        # print(i,j,flag)
        if flag:
            break
# print(check)
print("Yes" if not flag else "No")