#scenario qustion above. Select ... near file name

year = int(input("Enter a year: "))

# Check if the year is within the Gregorian calendar period (since 1582)
if year >= 1582:
    if ((year % 4 != 0) and (year % 400 != 0)):
        print ("Common year")
    
    elif (year % 100 != 0):
        print ("Leap year")
    
    else:
        print ("Leap year")

else:
    print("Not within the Gregorian calendar period")
