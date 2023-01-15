N = int(input())

user_list = []
changing_list = []
for _ in range(N):
  s, t = input().split()
  changing_list.append((s,t))
  user_list.append(s)
# print(user_list)
# print(changing_list)

def change_user_name(from_, to):
  user_list.pop(user_list.index(from_))
  user_list.append(to)

ans = "Yes"
index = 0

while len(changing_list) > 0:
  if index == len(changing_list):
    ans = "No"
    break
  from_ = changing_list[index][0]
  to = changing_list[index][1]
  if to not in user_list:
    changing_list.pop(index)
    change_user_name(from_, to)
    index = 0
  else: index += 1
  # print(index, len(changing_list), from_, to)
print(ans)