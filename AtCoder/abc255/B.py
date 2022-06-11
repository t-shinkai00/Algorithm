import math


N, K = map(int, input().split())
A = list(map(int, input().split()))
points = []
for _ in range(N):
  points.append(list(map(int, input().split())))
# print(points)

maximum = 0.0
for i, point in enumerate(points):
  if i+1 not in A:
    minimum = 10**10
    for lighter in A:
      # print(lighter, i+1)
      distance = math.sqrt((point[0] - points[lighter-1][0])**2 + (point[1] - points[lighter-1][1])**2)
      minimum = min(minimum, distance)
      if minimum < maximum:
        break
    maximum = max(maximum, minimum)

print('{:.12f}'.format(maximum))