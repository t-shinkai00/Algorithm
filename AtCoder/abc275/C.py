# https://atcoder.jp/contests/abc275/tasks/abc275_c
def index_Multi(List,liter):
  #Listはリスト本体・literは検索したい文字
  index_L = []
  for val in range(0,len(List)):
      if liter == List[val]:
          index_L.append(val)
  return index_L

def add_2d_tuple(a, b):
  return (a[0]+b[0], a[1]+b[1])

def is_square(i, j):
  global S
  start = S[i]
  next1 = S[j]
  vector = (next1[1]-start[1], start[0]-next1[0])
  next2 = add_2d_tuple(start, vector)
  next3 = add_2d_tuple(next1, vector)
  return next2 in S and next3 in S

S = []
for i in range(9):
  line = list(input())
  pones = index_Multi(line, "#")
  for el in pones:
    S.append((i, el))
# print(S)

cnt = 0
for i in range(len(S)):
  for j in range(i+1, len(S)):
    if is_square(i, j):
      cnt += 1
      # print(i,j)
print(cnt//2)
