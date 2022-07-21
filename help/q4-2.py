def discriminant(a,b,c):  # 2次方程式の判別式
  return b*b-4*a*c

for a in range(1,7):
  for b in range(1,7):
    for c in range(1,7):
      if discriminant(a,b,c) >= 0:
        print(a,b,c)