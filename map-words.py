list=["hello","world","my","name","is","Takahiro"]
def map(words,N):
    mapped=[]
    for word in words:
        print(int(word,36))
        mapped+=[int(word,36)%N]
    return mapped
print(map(list,3))