row1=input("enter first row numbers:").split()
row2=input("enter the other ow numbers:").split()
x=0
for i in range(8):
    if row1[i]=="1" and row2[i]=="1":
        x=x+1
print(f"it is {x}")