# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A
class Stack():
  def __init__(self):
    self.array = []
    self.len = 0
  def push(self, value):
    self.array.append(value)
    self.len += 1
  def pop(self):
    self.len -= 1
    if self.len<0:
      print("Error")
      exit()
    else:
      return self.array.pop(-1)

stack = Stack()
list=list(map(str,input().split()))
for c in list:
  if c == "+" or c == "-" or c == "*" or c == "/":
    post=stack.pop()
    prev=stack.pop()
    if c == "+":
      stack.push(prev+post)
    elif c == "-":
      stack.push(prev-post)
    elif c == "*":
      stack.push(prev*post)
    else:
      stack.push()
  else:
    stack.push(int(c))
print(stack.pop())