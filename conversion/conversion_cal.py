def sel():
    lbs = "lbs"
    kgs = "kgs"
    inches = "inches"
    unit = input("Please type lbs/kgs or inches for conversion: ")
   
    if unit == lbs:
         transfer = float(input("What is the weight in lbs? "))
         kg = 0.453592 * transfer
         
         if kg == 0:
             kg = 0.453592
         else:
             pass
         
         print("The weight is " + str(kg) + " Kilograms")
    
    elif unit == kgs:
        transfer = float(input("What is the weight in kgs? "))
        lbs = 2.20462 * transfer
        print ("The weight is " + str(lbs) + " Pounds.")
    
    elif unit == inches:
        transfer = float(input("What is the length in inches? "))
        cm = 2.54 * transfer
        print("The length is " + str(cm) + " Centimeters")
        
    else: 
        print("Incorrect unit of conversion")
        
sel()

