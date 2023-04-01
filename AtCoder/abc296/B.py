for i in range(8):
  string = list(input())
  if "*" in string:
    print(f'{chr(string.index("*")+97)}{8-i}')