# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_B
import math
a,b,C=map(float,input().split())
rad=math.radians(C)
S=a*b*math.sin(rad)/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
L=a+b+c
h=2*S/a
print(S)
print(L)
print(h)