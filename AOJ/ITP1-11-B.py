# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/11/ITP1_11_B
class Dice:
    def __init__(self):
        self.value=list(map(int,input().split()))
        self.num=int(input())

    def roll(self,direction):
        if direction=="N":
            self.value[0],self.value[1],self.value[4],self.value[5]=self.value[1],self.value[5],self.value[0],self.value[4]
        elif direction=="S":
            self.value[0],self.value[1],self.value[4],self.value[5]=self.value[4],self.value[0],self.value[5],self.value[1]
        elif direction=="E":
            self.value[0],self.value[2],self.value[3],self.value[5]=self.value[3],self.value[0],self.value[5],self.value[2]
        elif direction=="W":
            self.value[0],self.value[2],self.value[3],self.value[5]=self.value[2],self.value[5],self.value[0],self.value[3]

    def command(self):
        for i in range(self.num):
            top,front=map(int,input().split())
            if front==self.value[2] or front==self.value[3]:
                self.roll("W")
            while front!=self.value[1]:
                self.roll("N")
            while top!=self.value[0]:
                self.roll("W")
            self.print_face()

    def print_dice(self):
        print(self.value)
        print(self.command)

    def print_face(self):
        print(self.value[2])

dice1=Dice()
dice1.command()
# dice1.print_face()