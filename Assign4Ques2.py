'''A year is a leap year if it is divisible by 4, except that years divisible by 100 are not 
leap years unless they are also divisible by 400. Write a program that asks the user 
for a year and prints out whether it is a leap year or not.'''
#take input year
year = int(input("Enter year: "))

if year % 400 == 0 :
    print(year, "is a Leap Year")
elif year % 100 == 0 :
    print(year, "is not a Leap Year")
elif year % 4 == 0 :
    print(year, "is a Leap Year")
else :
    print(year, "is not a Leap Year")
#22105015
