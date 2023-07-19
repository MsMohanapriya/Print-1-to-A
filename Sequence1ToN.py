def Sequence1ToN(number):
    if number>0:
        Sequence1ToN(number-1)
        print(number,end=' ')
    return ''
        
number=int(input("enter number: "))
print(Sequence1ToN(number))