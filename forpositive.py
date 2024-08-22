import random
while True:
    num=random.randint(1,10)
    a=eval(input(f"say your first chance beween numbers 1 to 10:")) 
    if num==a:
        print("you won")
    elif a>num:
        print("say a smaller number")
        a=eval(input(f"say your secound chance beween numbers 1 to 10:")) 
        if num==a:
            print("you won")
        elif a>num:
            print("say a smaller number")
            a=eval(input(f"say your third chance beween numbers 1 to 10:")) 
            if a==num:
                print("you won")  
            else:
                print("you lost") 
        else:
            print("say a bigger number")
            a=eval(input(f"say your third chance beween numbers 1 to 10:")) 
            if a==num:
                print("you won")  
            else:
                print("you lost") 
    else:
        print("say a bigger number")
        a=eval(input(f"say your secound chance beween numbers 1 to 10:")) 
        if num==a:
            print("you won")
        elif a>num:
            print("say a smaller number")
            a=eval(input(f"say your third chance beween numbers 1 to 10:")) 
            if a==num:
                print("you won")  
            else:
                print("you lost") 
        else:
            print("say a bigger number")
            a=eval(input(f"say your third chance beween numbers 1 to 10:")) 
            if a==num:
                print("you won")  
            else:
                print("you lost") 

    
    
