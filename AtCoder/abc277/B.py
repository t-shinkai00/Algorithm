# https://atcoder.jp/contests/abc277/tasks/abc277_b
N = int(input())

S = []
str1 = ["H", "D", "C", "S"]
str2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
ans = "Yes"
for _ in range(N):
  line = input()
  if line in S or line[0] not in str1 or line[1] not in str2:
    ans = "No"
    break
  else:
    S.append(line)

print(ans)