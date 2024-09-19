person = int(input("Enter your age : "))

print("Choose for vote")
a = print("a = BJP")
b = print("b = BSP")
c = print("c = INC")
d = print("d = SP")

choice=input("Choose any one (a=BJP , b=BSP , c=INC , d=SP) : ")

if(person>=18):
    print("You are eligible to vote")

    if(choice=='a'):
        print("Your vote = (BJP)")

    else:
        if(choice=='b'):
            print("Your vote = (BSP)")

        else:
            if(choice=='c'):
                print("Your vote = (INC)")

            else:
                if(choice=='d'):
                    print("Your vote = (SP)")


else:
    print("Sorry! Yor are not eligible")


