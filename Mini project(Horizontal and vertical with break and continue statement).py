''' Make a mini project in which taking the input from user for (start point,end point,updation) and print the numbers either
reverse order or forward order in horizontal or vertical and also the (break) and (continue) statement '''



order = input("Type(r) for reverse , Type(f) for forward : ")
pattern = input("Type(h) for horizontal , Type(v) for vertical : ")
s = int(input("Enter starting value : "))
e = int(input("Enter ending value : "))
updation = int(input("Enter updation value : "))
B = int(input("Enter a Breaking point : "))
C = int(input("Enter a Continue point : "))


if((order=='f') and (pattern=='h')):
    for i in range (s,e+1,updation):
        if(i==B):
            break
        if(i==C):
            continue
        print(i,end=" ")

elif((order=='f') and (pattern=='v')):
    for i in range(s,e+1,updation):
        if(i==B):
            break
        if(i==C):
            continue
        print(i)

elif((order=='r') and (pattern=='v')):
    for i in range(s,e-1,-updation):
        if(i==B):
            break
        if(i==C):
            continue
        print(i)
        
elif((order=='r') and (pattern=='h')):
    for i in range (s,e-1,-updation):
        if(i==B):
            break
        if(i==C):
            continue
        print(i,end=" ")
        

else:
    print("Invalid value")
