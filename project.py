def firstsetbit(number):
    position=1
    mask=1
    while(not(number&mask)):
        mask=mask<<1
        position+=1
    return position
number=int(input("Enter a number:"))
print(firstsetbit(number))