def setornot(number,n):
    if number&(1<<(n-1)):
        print("\nSet")
    else:
        print("\nNotset")
number=int(input("Enter the number:"))
n=int(input("Enter the bit position:"))
setornot(number,n)