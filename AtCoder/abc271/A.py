num = int(input())
hex_ = hex(num)[2:].upper()
if len(hex_) == 1:
  hex_ = "0"+str(hex_)
print(hex_)