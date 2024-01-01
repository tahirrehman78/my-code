print("**Student Marksheet**")
name=input("Enter Student Name: ")
eng=eval(input("Enter English Marks: "))
urdu=eval(input("Enter urdu Marks: "))
math=eval(input("Enter Mathematics Marks: "))
comp=eval(input("Enter Computer Marks: "))
sci=eval(input("Enter Science Marks: "))
tot_marks=eng+urdu+math+comp+sci
print("Total Marks: ",tot_marks)
percentage=(tot_marks/500)*100
print(f"{percentage:.2f}")
if percentage>90:
    print("A+")
elif(percentage>90 and percentage<=80):
    print("A")
elif(percentage<80 and percentage>=70):
    print("B")
elif(percentage<70 and percentage>=60):
    print("C")
elif(percentage<60 and percentage>=50):
    print("D")
else:
    print("Fail")