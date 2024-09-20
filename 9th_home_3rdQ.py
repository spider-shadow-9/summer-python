def separator(ls):
    even=[]
    odd=[]
    for i in ls:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return f"even numbers{even},odd numbers:{odd}"
Input=input("say the numbers:")
listinput=Input.split(",")
List=list(map(int,listinput))
print(separator(List))