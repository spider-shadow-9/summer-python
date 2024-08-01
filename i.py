numbers=input("enter numbers:").split()
numbersint=list(map(int,numbers))
s=sum(numbersint)
del numbers[2]
if s%2==0:
    a=eval(input("enter a number"))
    print(s+a)
else:
    print(list(map(int,numbers)))
