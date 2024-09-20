def game(number):
    st1=int(number[0])
    nd2=int(number[1])
    if st1>nd2:
        return st1-nd2
    else:
        return nd2-st1
number=input("enter the number:")
print(game(number))