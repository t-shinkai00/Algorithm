# https://atcoder.jp/contests/abc257/tasks/abc257_a
n, x = map(int, input().split())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabets[(x-1)//n])