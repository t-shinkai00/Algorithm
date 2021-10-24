input=int(input())
# print(input)
A=[12,15,19,36,38,45,56,88,99]

# half=int(len(A)/2)
# print(A[:half])
# print(A[half:])

def BinarySearch(list,b):
    n=len(list)
    half=int(n/2)
    print(n)
    if list[half]==b:
        return True
    elif n==1:
        return False
    elif list[half]>b:
        return BinarySearch(list[:half],b)
    else:
        return BinarySearch(list[half:],b)

print(BinarySearch(A,input))