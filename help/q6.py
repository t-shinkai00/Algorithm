def prime(limit):
  yakusu=[0]*limit

  for i in range(2,limit):
    if yakusu[i] == 0:
      j = i
      while j < limit:
        yakusu[j] = i
        j = j + i

  num = 0
  for i in range(2,limit):
    if yakusu[i] == i:
      num = num + 1

  return num

print(prime(10))
print(prime(100))
print(prime(1000))
