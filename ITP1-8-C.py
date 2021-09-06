# https://srbrnote.work/archives/6003
count=[0]*(ord("z")-ord("a")+1)
while True:
    try:
        line=list(input().replace(" ","").replace(".",""))
        for i in range(len(line)):
            # print(line[i])
            count[ord(str(line[i]))-ord("a")]+=1
    except EOFError:
        break
for i in range(ord("z")-ord("a")+1):
    print(f"{chr(i+ord('a'))} : {count[i]}")