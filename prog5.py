## prog5.py
## Andrea Hsieh
## May 5th, 2016

## Problem 1
def printAverages(score):
    """function printAverage prints the average of each quiz scores excluding the lowest score
       parameter score is a 2D list of integers"""
##    scores = [[Quiz1Student1,Quiz1Student2,Quiz1Student3,Quiz1Student4,Quiz1Student5],
##              [Quiz2Student1,Quiz2Student2,Quiz2Student3,Quiz2Student4,Quiz2Student5],
##              [Quiz3Student1,Quiz3Student2,Quiz3Student3,Quiz3Student4,Quiz3Student5]]  
    for i in range(0,len(score)):
        # for each different quiz (row)
        total = 0
        for j in range(0,len(score[i])):
            # for each quiz score for each student (column)
            total = total + score[i][j]
            count = len(score[i]) - 1
        average = (total - min(score[i])) / count
        print("Average for row ", i, "is ", average)

## Problem 2
    
def addTables(list1,list2):
    """fucntion addTables add the numbers of two lists in the same postition together
       paramter list1 and list2 are both 2D lists"""
    
    total = list1
    addTotal = []
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            total[i][j] = list1[i][j] + list2[i][j]
    print(total)
