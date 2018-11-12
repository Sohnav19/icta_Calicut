num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))
num3=int(input("Enter the 3rd number : "))
if(num1>num2):
    if(num1>num3):
        print("large : ",num1)
    else:
        print("large : ",num3)
else:
    if(num2>num3):
        print("large : ",num2)
    else:
        print("latgr : ",num3)    
