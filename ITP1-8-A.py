input=input()
for i in range(len(input)):
    if str(input[i]).islower():
        input[i]=input[i].upper()
    elif str(input[i]).isupper():
        input[i]=input[i].lower()
for i in range(len(input)):
    print(input[i])