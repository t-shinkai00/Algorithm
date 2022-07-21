def discriminant(a,b,c):  # 2次方程式の判別式
  return b*b-4*a*c

def is_square(x):
  for i in range(x+1):
    if i * i == x:
      return True
  return False

for a in range(1,7):
  for b in range(1,7):
    for c in range(1,7):
      if discriminant(a,b,c) >= 0:
        if is_square(discriminant(a,b,c)):
          print(a,b,c)