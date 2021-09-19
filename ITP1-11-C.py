# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/11/ITP1_11_C
class Dice:
    def __init__(self):
        self.value=list(map(int,input().split()))

    def roll(self,direction):
        if direction=="N":
            self.value[0],self.value[1],self.value[4],self.value[5]=self.value[1],self.value[5],self.value[0],self.value[4]
        elif direction=="S":
            self.value[0],self.value[1],self.value[4],self.value[5]=self.value[4],self.value[0],self.value[5],self.value[1]
        elif direction=="E":
            self.value[0],self.value[2],self.value[3],self.value[5]=self.value[3],self.value[0],self.value[5],self.value[2]
        elif direction=="W":
            self.value[0],self.value[2],self.value[3],self.value[5]=self.value[2],self.value[5],self.value[0],self.value[3]

    def command(self,target):
        order="NNNNWNNNWNNNENNNENNNWNNN"
        flag=False
        if self.value==target:
                flag=True
        for i in range(len(order)):
            self.roll(order[i])
            if self.value==target:
                flag=True
                break
        print("Yes" if flag else "No")

    def print_dice(self):
        print(self.value)

    def print_face(self):
        print(self.value[2])

dice1=Dice()
dice2=Dice()
dice2.command(dice1.value)