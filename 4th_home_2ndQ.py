year=int(input("Enter the year:"))
if year%4==0:
    print("it is leap")
elif year%4==0 and year%100==0:
    print("it is not leap")
else:
    print("it is not leap")