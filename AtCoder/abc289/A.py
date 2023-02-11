# https://atcoder.jp/contests/abc289/tasks/abc289_a
s = input()
for bit in s:
  if bit == "0":
    print("1", end="")
  else:
    print("0", end="")
print()