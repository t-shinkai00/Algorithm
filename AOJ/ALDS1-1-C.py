# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_C
import math
def is_prime(x):
    if x==2 or x==3:
        return True
    for i in range(2,math.floor(math.sqrt(x))+1):
        # print(i)
        if x%i==0:
            return False
    return True

cnt=0
n=int(input())
for i in range(n):
    x=int(input())
    if is_prime(x):
        cnt+=1
print(cnt)