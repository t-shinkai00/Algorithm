# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A
num_V,num_E,r=map(int,input().split())

class AdjacencyList():
  def __init__(self,n):
    self.arr=[]
    for i in range(n):
      self.arr.append([])
  def add_edge(self,s,t,d):
    self.arr[s].append([t,d])


def djikstra(list,r):
  global num_V
  distances=[99999]*num_V  # INF
  # print(distances)
  visited=[]
  visited.append(r)
  distances[r]=0  # initial conditions
  while len(visited)<num_V:
    min=99999
    flag=False
    for vertex in visited:
      for edge in list[vertex]:
        to=edge[0]
        weight=edge[1]
        if weight+distances[vertex]<min:
          min=weight+distances[vertex]
          min_from=vertex
          min_to=to
          flag=True
    if flag==True:
      if min<distances[min_to]:  #update distance
        distances[min_to]=min
      if not min_to in visited:
        visited.append(min_to)
      # min_from=min_to
      for (i,element) in enumerate(list[min_from]):
        if element[0]==min_to:
          del list[min_from][i]
          # print(min_from,min_to,distances[min_from],distances[min_to])
          # print("------------------------------------------------------------------------------")
          # print(list)
    else:
      break
  # print(list)
  # print(visited)
  return distances

list=AdjacencyList(num_V)
# print(list.arr)
for i in range(num_E):
  s,t,d=map(int,input().split())
  list.add_edge(s,t,d)
# print(list.arr)
distances=djikstra(list.arr,r)
for distance in distances:
  if distance != 99999:
    print(distance)
  else:
    print("INF")