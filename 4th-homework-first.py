speed=eval(input("Enter speed:"))
if speed<90:
    print("No ticket!")
elif speed>=91 and speed<=110:
    print("Small ticket!")
else:
    print("Big ticket!")