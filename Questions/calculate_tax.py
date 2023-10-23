#select the ... abov - right of the file name to see scenario

income = float(input("Enter the annual income: "))

if (income <= 85528):
    tax = ((income *.18) - 556.02)
    if (tax < 0):
        tax = 0.0
    
    
elif (income >= 85528):
    tax = (((income - 85528)*.32) + 14839.02)
    

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
