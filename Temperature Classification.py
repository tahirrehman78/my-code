'''Temperature Classification:
Write a program that takes an input temperature from the user and classifies it as:

"Freezing" if below 0°C
"Cold" if between 0°C and 15°C
"Moderate" if between 16°C and 30°C
"Hot" if above 30°C
'''

# Temperature Classification
temp=eval(input("Enter temperature:"))
if temp<0:
          print("It's Freezing today")
elif (temp>=0 and temp<=15):
    print("It's Cold today")
elif (temp>15 and temp<=30):
    print("It's Moderate today")
else:
    temp>30
    print("It's Hot today")