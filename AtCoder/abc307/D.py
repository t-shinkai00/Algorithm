# https://atcoder.jp/contests/abc307/tasks/abc307_d
n=int(input())
S=input()

from queue import LifoQueue

s=LifoQueue()
i=0
while i<len(S):
    if S[i] == "(":
        s.put(i)
    elif S[i] == ")" and not s.empty():
        i_start = s.get()
        S = S[:i_start]+S[i+1:]
        i = i_start-1
    i += 1
print(S)