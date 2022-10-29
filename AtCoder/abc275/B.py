# https://atcoder.jp/contests/abc275/tasks/abc275_b
A, B, C, D, E, F = map(int, input().split())
numerator = (A*B*C)-(D*E*F)
denominator = 998244353
print(numerator%denominator)