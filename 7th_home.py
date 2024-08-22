print("============MAIN MENU============")
print("1-Create new contact")
print("2-Edit Contact")
print("3-Delete Contact")
print("4-Block Contact")
print("5-Show contacts")
print("6-Call")
while True:
    item=input("choose an item:")
    if item=="1":
        a=open("contacts.txt","a")
        name=input("enter the name:")
        phone=input("enter the phone number:")
        a.write(f"\n{name}:{phone}\n")
        a.close()
    elif item=="2":
        x=input("you wanna edit phone name?:")
        a=open("contacts.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        if x=="phone":
            d=input("enter the name:")
            r=input("enter the  new phone number:")
            dictionary[d]=r
            a1=open("contacts.txt","w")
            for i in dictionary:
                a1.write(f"\n{i}:{dictionary[i]}\n")
            a1.close()
        elif x=="name":
            name=input("enter the new name:")
            phone=input("enter the phone number:")
            l_name=input("enter the lastest name:")
            del dictionary[l_name]
            dictionary[name]=phone
            a1=open("contacts.txt","w")
            for i in dictionary:
                a1.write(f"\n{i}:{dictionary[i]}\n")
            a1.close()
    elif item=="3":
        delete=input("enter the name:")
        a=open("contacts.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        del dictionary[delete]
        a1=open("contacts.txt","w")
        for i in dictionary:
            a1.write(f"\n{i}:{dictionary[i]}\n")
        a1.close()
    elif item=="4":
        name=input("enter the name of person:")
        a=open("contacts.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        if name in dictionary:
            x=open("blocked.txt","a")
            x.write(f"\n{name}")
            x.close()
        else:
            pass
    elif item=="5":
        a=open("contacts.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
            for i in dictionary:
                print(i,dictionary[i])
    elif item=="6":
        a=open("contacts.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        a=open("blocked.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        a.close()
        x=input("enter the name:")
        if x in dictionary:
            if x in c:
                l=input("the name is in blockes unblock it or no?:")
                if l=="yes":
                    c.remove(x)
                    s=open("blocked.txt","w")
                    for i in c:
                        s.write(f"\n i")
                    print(f"calling {x}...")
                else:
                    print("you can't call this contact because of blocking him\her")
            else:
                print(f"calling {x}...")
        else:
            print("you haven't got this contact")