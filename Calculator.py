# menus
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a+b
    print("Add = ",c)
elif ch==2:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a-b
    print("Subtract = ",c)
elif  ch==3:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a*b
    print("Multiply = ",c)
elif ch==4:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    c=a/b
    print("Division = ",c)
else:
    print("Invalid Choice")