class Dice:
    def __init__(self):
        self.value=list(map(int,input().split()))
        self.command=input()

    def roll(self):
        for i in range(len(self.command)):
            if self.command[i]=="N":
                self.value[0],self.value[1],self.value[4],self.value[5]=self.value[1],self.value[5],self.value[0],self.value[4]
            elif self.command[i]=="S":
                self.value[0],self.value[1],self.value[4],self.value[5]=self.value[4],self.value[0],self.value[5],self.value[1]
            elif self.command[i]=="E":
                self.value[0],self.value[2],self.value[3],self.value[5]=self.value[3],self.value[0],self.value[5],self.value[2]
            elif self.command[i]=="W":
                self.value[0],self.value[2],self.value[3],self.value[5]=self.value[2],self.value[5],self.value[0],self.value[3]

    def print_dice(self):
        print(self.value)
        print(self.command)
        print(self.x,self.y)

    def print_face(self):
        print(self.value[0])

dice1=Dice()
dice1.roll()
dice1.print_face()