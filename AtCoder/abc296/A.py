N = int(input())
S = input()

def check_alternately(num, string):
  before = ""
  for i in range(num):
    if string[i] == before: return False
    before = string[i]
  return True

if check_alternately(N,S): print("Yes")
else: print("No")