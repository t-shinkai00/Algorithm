def calc_num(alpabet):
  return ord(alpabet)-64

S = list(input())
nums = list(map(calc_num, S))

num = 0
for i, el in enumerate(nums):
  num += 26**(len(nums)-i-1)*el
print(num)