# https://atcoder.jp/contests/abc257/tasks/abc257_d
import sys
import math


class Jump():
  def __init__(self, x, y, p):
    self.x = x
    self.y = y
    self.power = p

n = int(input())

jumps = []
for _ in range(n):
  x, y, p = map(int, input().split())
  jump = Jump(x, y, p)
  jumps.append(jump)

max_needed = 0
for el1 in jumps:
  min_needed = sys.maxsize
  for el2 in jumps:
    if el1 != el2:
      min_needed = min(min_needed, (abs(el1.x-el2.x)+abs(el1.y-el2.y))/max(el1.power,el2.power))
  max_needed = max(max_needed, min_needed)
print(math.ceil(max_needed))