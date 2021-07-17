pairsA = [["a", 1], ["b", 2], ["c", 3]]
pairsB = [["b", 3], ["d", 4]]
def merge(A,B):
    ans=B
    for s in range(len(A)):
        for t in range(len(ans)):
            if A[s][0]==ans[t][0]: # もし同じwordが含まれるなら
                ans[t][1]+=A[s][1]
                break
        else: # 含まれていなければ
            ans+=[A[s]]
    return ans
print(merge(pairsA,pairsB))