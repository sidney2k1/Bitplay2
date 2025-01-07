#program to find the number of zero bits and one bits in a number
#function taking our number as input
def numberofbits(n):
    ones=0
    zero=0
    while(n):
        if(n&1==1):
            ones+=1
        else:
            zero+=1
        n>>=1
    print("\nOnes=",ones,"\nzeros=",zero)
number=int(input("Entar the number:"))
numberofbits(number)