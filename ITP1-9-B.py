# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/9/ITP1_9_B
while True:
    word=input()
    if word=="-":
        break
    m=int(input())
    for i in range(m):
        h=int(input())
        a=word[:h]
        b=word[h:]
        word=b+a
    print(word)