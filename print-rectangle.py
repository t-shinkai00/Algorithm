while True:
    H,W=map(int,input().split())
    if H==0 and W==0:
        break
    for y in range(H):
        for x in range(W):
            print("#",end="")
        print()