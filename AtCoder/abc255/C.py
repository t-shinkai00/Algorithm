import numpy as np


target, first, tolerance, num = map(int, input().split())
if tolerance < 0:
  first += tolerance*(num-1)
  tolerance = -tolerance
final = first + tolerance * (num - 1)

if target <= first:
  print(first-target)
elif final <= target:
  print(target-final)
else:
  print(min((target-first)%tolerance, tolerance-(target-first)%tolerance))