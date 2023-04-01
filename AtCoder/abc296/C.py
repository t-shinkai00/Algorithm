N, X = map(int, input().split())
A = list(map(int, input().split()))

def is_exist_gap(num, gap, arr):
  if gap == 0: return True
  candidates = []
  checked = []
  for i in range(num):
    if arr[i] in checked:
      continue
    if arr[i] in candidates:
      return True
    else:
      candidates.append(arr[i]-gap)
      candidates.append(arr[i]+gap)
      checked.append(arr[i])
  return False

if is_exist_gap(N, X, A): print("Yes")
else: print("No")