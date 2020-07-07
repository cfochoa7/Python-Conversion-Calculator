def sel():
    lbs = "lbs"
    kgs = "kgs"
    unit = input("Please type lbs or kgs for conversion: ")
   
    if unit == lbs:
         transfer = float(input("What is the weight in lbs? "))
         kg = 0.453592 * transfer
         print("The weight is " + str(kg) + " Kilograms")
    
    elif unit == kgs:
        transfer = float(input("What is the weight in kgs? "))
        lbs = 2.20462 * transfer
        print ("The weight is " + str(lbs) + " Pounds.")
        
    else: 
        print("Incorrect unit of conversion")
        
sel()

