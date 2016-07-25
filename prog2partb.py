## prog2partb.py
## Andrea Hsieh
## April 13th 2016
##
## Homework assignmetn 2 part b


## Problem 3

def inchesToMeters(inches):
    """function inchesToMeter converts inches to meters
       parameter inches is the value you want to convert to meters"""
    conversion_rate = 0.0254
    meters = inches * conversion_rate
    return meters


## Problem 4

def poundsToKgs(pounds):
    """function poundsToKgs converts pounds to kilograms
       parameter pounds is the value you want to convert to kilograms"""
    conversion_rate = 0.453592
    kgs = pounds * conversion_rate
    return kgs


## Problem 5

def bmi(meters,kgs):
    """function bmi calculates the body mass index
       parameter meters is height in meters
       parameter kgs is the weight in kilograms"""
    result = kgs/pow(meters,2)
    return result


## Problem 6

def bmiCategory(result):
    """funtion bmiCategory categorizes the value given into
       underwieght, normal weight, overweight, and obese.
       parameter result is the bmi value to be categorized"""
    if result < 18.5:
            result = "underweight"
            return result
            
    elif result < 25 and result >= 18.5:
            result = "normal weight"
            return result
            
    elif result < 30 and result >= 25:
            result = "overweight"
            return result
            
    elif result >= 30:
            result = "obese"
            return result

            
def bodyMassIndex():
    name = input("Please enter the subject's name: ")
    inches = float(input("Please enter the subject's height in inches: "))
    pounds = float(input("Please input the subject's weight in pounds: "))
    meters = inchesToMeters(inches)
    kgs = poundsToKgs(pounds)
    body_mass_index = bmi(meters,kgs)
    print(name, "has a body mass index of", body_mass_index)
    print(name, "is",bmiCategory(body_mass_index))
                   
bodyMassIndex()

