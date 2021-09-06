# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_A
line=list(map(str,input()))
for i in range(len(line)):
    if line[i].isupper():
        line[i]=line[i].lower()
    elif line[i].islower():
        line[i]=line[i].upper()
for i in range(len(line)):
    print(line[i],end='')
print()