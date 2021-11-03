# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A
class Queue():
  def __init__(self):
    self.array = []
    self.size = 0
  def enqueue(self, value):
    self.array.append(value)
    self.size += 1
  def dequeue(self):
    self.size -= 1
    if self.size<0:
      print("Error")
      exit()
    else:
      return self.array.pop(0)

class Process():
  def __init__(self,name,time):
    self.remaining = time
    self.name = name

queue = Queue()
n,q=map(int,input().split())
time=0

for i in range(n):
  p_name,p_time = input().split()
  process=Process(p_name,int(p_time))
  queue.enqueue(process)

while queue.size>0:
  process=queue.dequeue()
  # print(process.name,process.remaining)
  if process.remaining<=q:
    time+=process.remaining
    print(process.name,time)
  else:
      time+=q
      process.remaining-=q
      # print(process.name,process.remaining)
      queue.enqueue(process)