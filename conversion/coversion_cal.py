def convert():
    transfer = float(input("What is the weight in lbs? "))
    kg = 0.453592 * transfer
    print("The weight is  " + str(kg) + " kilograms")


convert()