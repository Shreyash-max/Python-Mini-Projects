''' Make a mini project for simple calculator '''


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Choice= (+ , - , * , /)")
choice=str(input("Choose any one= "))

if(choice=='+'):
    sum=a+b
    print("Addition is = ",sum)

elif(choice=='-'):
    sub=a-b
    print("Subtraction is = ",sub)

elif(choice=='*'):
    multi=a*b
    print("Multiplication is = ",multi)

elif(choice=='/'):
    div=a/b
    print("Division is = ",div)

else:
    print("Invalid value")

