from optparse import Values
import sys


n = int(input())
s = input()
W = list(map(int, input().split()))

values = []
for i in range(n):
  values.append((int(s[i]), W[i]))
values.sort(key= lambda x: x[1])
# print(values)

cnt = s.count("1")
maximum = cnt
former_weight = 0
for i, el in enumerate(values):
  if el[0] == 1:
    cnt -= 1
  else:
    cnt += 1
  if i == len(values)-1 or el[1] != values[i+1][1]:
    maximum = max(maximum, cnt)
    former_weight = el[1]
print(maximum)