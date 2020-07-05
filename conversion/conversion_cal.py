def sel():
    lbs = "lbs"
    unit = input("Please type lbs for conversion: ")
   
    if unit == lbs:
         transfer = float(input("What is the weight in lbs? "))
         kg = 0.453592 * transfer
         print("The weight is  " + str(kg) + " Kilograms")
        
    else: 
        print("Incorrect unit of conversion")
        
sel()

