n = int(input())
s = list(input())

bracketed = False
for i in range(n):
  if s[i] == "," and not bracketed:
    s[i] = "."
  elif s[i] == '"':
    bracketed = not bracketed
print("".join(s))