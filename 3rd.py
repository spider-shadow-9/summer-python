x=input("enter the colors:")
g=x.count("G")
y=x.count("Y")
r=x.count("R")
if r==5 or y==5 or r>=3 or r>=2 and y>=2:
    print("nakhor lite")
elif g==0 and r==0 and y==0:
    print("Error")
else:
    print("rahat baash")
