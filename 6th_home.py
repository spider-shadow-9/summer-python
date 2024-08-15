
# x=name , y=phone how you can enter something
#create : add x y
#edit name : edit name x x(new x) , edit phone : edit phone x y(new phone)
#delete : delete x
#block : block x
#show : show
#call : call x
#you can write and want only this items; Good Luck:)
contacts = {}
blocked = []
while True:
    put=input(":")
    put_l=put.split()
    if put_l[0]== "add":
        name=put_l[1]
        phone=put_l[2]
        contacts[name]=phone
    elif put_l[0]=="edit":
        if put_l[1]=="name":
            if put_l[2]in contacts.keys():
                n_name=put_l[3]
                contacts[n_name]=contacts[put_l[2]]
                del contacts[put_l[2]]
            else:
                print("you haven't got this contact")
        elif put_l[1]=="phone":
            if put_l[2] in contacts.keys():
                n_phone=put_l[3]
                contacts[put_l[2]]=n_phone
            else:
                print("you haven't got this contact")
    elif put_l[0]== "delete":
         if put_l[1] in contacts.keys():
              del contacts[put_l[1]]
    elif put_l[0]=="block":
         if put_l[1] in contacts.keys():
              blocked.append(put_l[1])
    elif put_l[0]=="show":
         for i in contacts:
              print(i,contacts[i])
    elif put_l[0]=="call":
        if put_l[1] in contacts.keys():
            if put_l[1] in blocked:
                if "unblock" in put_l:
                    blocked.remove(put_l[1])
                    print(f"calling{contacts[put_l[1]]}")
                else:
                    print(f"{put_l[1]}is block")
            else:
                print(f"calling {contacts[put_l[1]]}...")
        else:
            pass