H, W = map(int, input().split())

first = False
for i in range(H):
  line = input()
  points = [i for i, x in enumerate(line) if x == 'o']
  if len(points) == 2:
    print(abs(points[0]-points[1]))
    break
  elif len(points) == 1:
    if not first:
      h, w = i, points[0]
      first = True
    else:
      print(abs(points[0]-w)+abs(i-h))