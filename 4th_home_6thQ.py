numbers=input("Enter five numbers(put(,)between the numbers):").split(",")
num=list(map(int,numbers))
Sum=sum(num)

if Sum%2==0:
    n=eval(input("please enter a number:"))
    print(f"sum of them is: {Sum+n}")
else:
    x=Sum-num[2]
    print(f"sum of them is: {x}")