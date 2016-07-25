## prog3.py
## Andrea Hsieh
## April 24 2016
##

## Problem 1

def sumOfOdds(limit):
    """the function sumOfOdds add all the odd numbers together till the limit.
       limit is the limit of the odd numbers added together"""
    counter = 1
    total = 0
    while counter <= limit:
        total = total + counter
        counter = counter + 2
    return total
            
## Problem 2

def productOfPowersOf2(exp1,exp2):
    """function productOfPowersOf2 takes the product of all the exponents from exp1 to exp2
       exp1 is minimun exponent number and exp2 is the max""" 
    total = 1
    pow1 = exp1
    while pow1 <= exp2:
        total = total * (2**pow1)
        pow1 = pow1 + 1
    return total


## Problem 3

def printAsterisks(limit):
    """functioin printAsterisks prints asterisks a certain number of times.
       limit is the number of asterisks you want to print."""
    print("*" * limit)

## Problem 3(loop way)
## the function name doesn't have an "s" at the end

def printAsterick(limit):
    """functioin printAsterisks prints asterisks a certain number of times.
       limit is the number of asterisks you want to print."""
    number = 0
    result = ""
    while number < limit:
        result = result + "*" 
        number = number + 1

    print(result)


## Problem 4
    
def printTriangle(limit):
    """function printTriangle prints a right triangle of asterisks.
       limit is the height and width of the right triangle."""
    number = 1
    while number <= limit:
        print("*" * number)
        number = number + 1

## Problem 5

def allButMax():
    """funtion allButMax adds all the given numbers together but the max value."""
    input_string = input("Enter next number: ")
    if (input_string!="end" ):
        number = float(input_string)
        
    total = 0
    max_num = 0
    
    while input_string != "end" and number >= 0:
        if (number > max_num):
            max_num = number
        else:
            max_num = max_num  
        total = total + number
        input_string = input("Enter next number: ")
        
        if (input_string!="end" ):
            number = float(input_string)
  
    total = total - max_num
    print("The sum of all values except for the maximum value is: ",total)
    return total
    

## Problem 6

def avgSumOfSquares():
    """function avgSumOfSquares computes the average of the sum of the squares
       of all the values entered."""
    input_string = input("Enter next number: ")
    if input_string == "end":
        print("No numbers were entered.")
        
    else:
        total = 0
        counter = 0

        while input_string != "end":
            number = float(input_string)
            number = pow(number,2)
            counter = counter + 1
            total = total + number
            input_string = input("Enter next number: ")
        
        average = total / counter
        print("The average of the sum of the squares is: ",average)
    return average
    


        
        
