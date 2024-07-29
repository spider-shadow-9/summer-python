num=eval(input("Enter a number:"))
num_0=str(num)
num_1=num_0[::-1]
num_2=int(num_1)
if num==num_2:
    print("Inverted")
else:
    print("Non-inverted")