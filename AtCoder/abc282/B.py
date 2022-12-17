n, m = map(int, input().split())

def is_all_correct(a, b, m):
  for i in range(m):
    if a[i] == "x" and b[i] == "x":
      return False
  return True

cnt = 0
participants = []
for _ in range(n):
  participant = input()
  for member in participants:
    if is_all_correct(participant, member, m):
      # print(participant, member)
      cnt += 1
  participants.append(participant)
print(cnt)