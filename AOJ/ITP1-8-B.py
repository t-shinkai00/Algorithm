# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_B
while True:
    line=input()
    if len(line)==1 and line[0]=="0":
        break
    count=0
    for i in range(len(line)):
        count+=int(line[i])
    print(count)