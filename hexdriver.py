## hexdriver.py
## version 0.1
## May 20, 2016

## Here's the crude, unpolished first version of a user
## interface for your hexapawn function

## It doesn't really know much about who wins the game
## or when...although it does know that if it can't make
## a move, the human player wins.

## It does not validate the coordinates for the move
## that is entered by the user.  You can move any pawn
## on either side to any square.  So be careful.

## your definitions for generateMoves and
## chooseBestMove go up here
## prog67.py
## Andrea Hsieh
## 5/31/15
## hw #6 and 7 hexapawn


## below is what we supply ======================================


## print a board
## 0 prints as '-', 1 prints as 'w', 2 prints as 'b'

def printBoard(board):
    print("   ", end = "")
    for i in range(0, len(board[0])):
        print(str(i)+" ", end = "")

    print("\n")
    row = 0
    for r in board:
        print(row, " ", end = "")
        for c in r:
            if c == 1:
                print("w ", end = "")
            elif c == 2:
                print("b ", end = "")
            else:
                print("- ", end = "")
        print()
        row = row + 1
    print()
            

## create an initial board, with dimension
## passed as the argument. 1s at the top,
## 2s at the bottom, 0s everywhere else
    
def makeInitBoard(dim):
    board = []
    for i in range(0,dim):
        row = []
        for j in range(0,dim):
            row.append(0)
        board.append(row)

    for i in range(0,dim):
        board[0][i] = 1
        board[dim - 1][i] = 2
        
    return board


## this is the user interface for the hexapawn game.
## just run the program and type 'hexapawn()' in the
## interaction window

def hexapawn():
    from random import randint

    print("Welcome to Hexapawn")

    ## ask for board size and create initial board
    
    dim = int(input("What size board would you like? \n(enter an integer greater than 2): "))
    bheight = dim
    bwidth = dim
    b = makeInitBoard(dim)
    
    print("\nHere's the initial board...\n")
    
    printBoard(b)

    ## ask user to select color of pawns
    ## if user selects white, then the program's color is 2 (i.e., black)
    ## if user selects black, then the program's color is 1 (i.e., white)

    while True:
        answer = input("Choose the white pawns or black pawns (enter 'w' or 'b' or 'quit'): ")
        if answer == "w":
            mycolor = 2
            break
        if answer == "b":
            mycolor = 1
            break
        if answer == "quit":
            print("Ending the game")
            return

    ## if program has white pawns, generate program's first move

    if mycolor == 1:
        print("Here's my opening move...\n")
        column = randint(0, bwidth - 1)
        b[1][column] = b[0][column]
        b[0][column] = 0
        printBoard(b)

    ## game loop

    while True:
        
        ## ask for user's move
        ## coordinates are not validated at this time
        
        print("\nEnter the coordinates of the pawn you wish to move:")
        fromrow = int(input("   row: "))
        fromcol = int(input("   col: "))
        print("Enter the coordinates of the destination square: ")
        torow = int(input("   row: "))
        tocol = int(input("   row: "))
        b[torow][tocol] = b[fromrow][fromcol]
        b[fromrow][fromcol] = 0
        print("This is your move...\n")
        printBoard(b)

        ## here is where the program uses the functions created by the student
        
        possiblemoves = generateMoves(mycolor, b)  # don't change this function call
        if possiblemoves == []:
            print("I can't move\nCongratulations! You win!")
            return
        b = chooseBestMove(mycolor, possiblemoves) # don't change this function call


        print("Here's my response...\n")
        printBoard(b)




