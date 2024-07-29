List=input("enter question:").split()
num_1=int(List[0])
num_2=int(List[2])
match List[1]:
    case "+":
        print(f"sum={num_1+num_2}")
    case "-":
        print(f"minus={num_1+num_2}")
    case "*":
        print(f"multiple={num_1*num_2}")
    case "//":
        print(f"divide={num_1//num_2}")
    case "%":
        print(f"remainder={num_1%num_2}")