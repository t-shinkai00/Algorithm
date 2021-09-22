# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_B
def gcd(x,y):
    if x>y:
        if x%y==0:
            return y
        return gcd(y,x%y)
    else:
        if y%x==0:
            return x
        return gcd(x,y%x)
x,y=map(int,input().split())
print(gcd(x,y))