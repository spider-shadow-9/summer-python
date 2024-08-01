nums=input("enter 5 numbers:").split()
print(nums)
num=list(map(int,nums))
s=sum(num)
if s%2==0:
    n=eval(input())
    print(s+n)
else:
    x=nums.pop(2)
    print(list(nums.remove("x")))