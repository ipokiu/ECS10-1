## prog4.py
## Andrea Hsieh
## May 2, 2016

# Problem 1

def sumOfOdds(limit):
    """the funtion sumOfOdds funds the sum of all the odds number up the limit
       parameter limit is the max number to add odd numbers up to"""
    
    total = 0
    
    for number in range(1,limit + 1,2):
        total = total + number
        
    return total

# Problem 2

def countChar(character, string):
    """the funtion countChar counts the number of times a character appears in a sting
       paramter character is the character that is being count
       paramter string is the string to count characters from"""
    count = 0
    for char in string:
        if char == character:
            count = count + 1
        else:
            pass
    return count
        
# Problem 3

def countDiffs(string1,string2):
    """the function countDiffs compares two strings
       and counts the number of times the two strings have different characters in the same location
       paramter string1 and string2 are the two strings you want to compare"""
    count = 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            count+=1
    return count

# Program 4

def avgSumOfSquares(numbers):
    """the funtion avgSumOfSquares finds the average of the squares of each number
       the parameter numbers is a list of all the numbers you want to square and find the average of"""
    count = 0
    total = 0
    for i in numbers:
            num = i**2
            count+=1
            total = total + num
    if count == 0:
        return None
    else:
        return total/count


# Program 5

def morseCode():
    """the function morseCode translates a string into morse code"""
    morseString = ''
    morse_code = [["a",".-"],["b","-..."],["c","-.-."],["d","-.."],
                  ["e","."],["f","..-."],["g","--."],["h","...."],
                  ["i",".."],["j",".---"],["k","-.-"],["l",".-.."],
                  ["m","--"],["n","-."],["o","---"],["p",".--."],
                  ["q","--.-"],["r",".-."],["s","..."],["t","-"],
                  ["u","..-"],["v","...-"],["w",".--"],["x","-..-"],
                  ["y","-.--"],["z","--.."]]
    input_string = input("Enter sentence to be translated (*** to end): ")
    if input_string != "***":
        
        for i in range(0,len(input_string)):
            # iterates through every character in the string
            if input_string[i] == ' ':
                morseString = morseString+ ' '
                # condition for character is a space
            else:
                for j in range(0,len(morse_code)):
                    # iterates 26 times(alphabet)
                       if input_string[i] == morse_code[j][0]:
                           # compares input character to first element in the list inside the list
                           morseString = morseString + morse_code[j][1] + ' '
                           # appends morse string (second element in the list inside the list)
                           break
                      
                       elif j == 25:
                           morseString = morseString + '### '
                           # condition for input character not matching morse_code library entries
                           
        print(morseString)

    else:    
        print("Program has ended")
        

        
