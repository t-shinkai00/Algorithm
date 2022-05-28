def main(a, b, c):
  if a <= b and b <= c or c <= b and b <= a:
    print("Yes")
  else:
    print("No")

if __name__=="__main__":
  a,b,c = map(int, input().split())
  main(a, b, c)