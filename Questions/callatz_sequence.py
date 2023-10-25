num = int(input("enter a natural number "))
count = 0

while num > 1:

    if num % 2 == 1:
        num = num * 3 + 1
        print(num)
    
    elif num % 2 == 0:
        num = num // 2
        print(num)
        count +=1
        
if num == 1:
    print("steps = ", count)
        
else:
    print("that's not an natural number") 
