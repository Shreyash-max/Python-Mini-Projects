while True:
    S = input("Type y for continue or n for exit : ")
    if(S.lower()=='y'):

        age = int(input('Enter your age : '))
        if(age>=18):
            print("You are eligible, Please proceed")
        
            print("Choose any one-")
            a = print("a = BJP")
            b = print("b = BSP")
            c = print("c = INC")
            d = print("d = SP")

            choice = input("Vote any one : ")

            if(choice=='a'):
                print('Your vote goes to (BJP)')
            elif(choice=='b'):
                print('Your vote goes to (BSP)')
            elif(choice=='c'):
                print('Your vote goes to (INC)')
            elif(choice=='d'):
                print('Your vote goes to (SP)')
        elif(age<=17):
            print('You are not eligible')
            break        
    elif(S.lower()=='n'):
        break
    else:
        print('Invalid choice')
