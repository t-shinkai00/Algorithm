S=int(input())
sec=S%60
min=(S%3600)//60
hour=S//3600
print(f"{hour}:{min}:{sec}")