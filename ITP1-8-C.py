# https://srbrnote.work/archives/6003
count=[0]*(ord("z")-ord("a")+1)
while True:
    try:
        line=list(input().replace(" ","").replace(".",""))
        for i in range(len(line)):
            # print(line[i])
            if 0<=ord(line[i].lower())-ord("a")<=ord("z")-ord("a"):
                count[ord(line[i].lower())-ord("a")]+=1
    except EOFError:
        break
for i in range(ord("z")-ord("a")+1):
    print(f"{chr(i+ord('a'))} : {count[i]}")