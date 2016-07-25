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
## prog67.py
## Andrea Hsieh
## 5/31/15
## hw #6 and 7 hexapawn


def generateMoves(color, board):
    """
    This function generates all the possible moves for a color. 
    paramter color is the color that has the next move
    parameter board is a list of list, 0 is empty space, 1 is white pawn, 2 is black pawn
    """
    import copy
    newboard = copy.deepcopy(board)
    moves = []

    if color == 1:
        for r in range(len(board)):## r: row index
            for c in range(len(board[r])):## c: column index
                if board[r][c] == 1:
                    if c == 0: ## left-most column, check top, top-right only
                        if r < len(board): ## not at board's bottom row
                            if board[r+1][c] == 0: ## down one is a valid spot to move in
                                newboard[r+1][c] = 1
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board) #reset board to original for next if statement
                            if board[r+1][c+1] == 2: ## down-right is a valid spot to move
                                newboard[r+1][c+1] = 1  
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                    else: ##if c > 0 i.e. other columns, consider down-left, down, down-right
                        if r < len(board): ## not at board's bottom row
##                            print('r',r)
                            if board[r+1][c-1] == 2: ## down-left is a valid spot to move
                                newboard[r+1][c-1] = 1
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                            if board[r+1][c] == 0: ## down is a valid spot to move
                                newboard[r+1][c] = 1
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                            if c+1 < len(board):
                                if board[r+1][c+1] == 2: ## down-right is a valid spot to move
                                    newboard[r+1][c+1] = 1
                                    newboard[r][c] = 0
                                    moves.append(newboard)
                                    newboard = copy.deepcopy(board)
                                
    newboard = copy.deepcopy(board)
    if color == 2:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 2:
                    if c == 0: #left most column
                        if r > 0: #not at top of board
                            if board[r-1][c] == 0: #move up
                                newboard[r-1][c] = 2
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                            if board[r-1][c+1] == 1: #move up-right
                                newboard[r-1][c+1] = 2
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                    else: # c > 0. not the most left column
                        if r > 0: # not at top row
                            if board[r-1][c] == 0: #move up
                                newboard[r-1][c] = 2
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                            if board[r-1][c-1] == 1: #move up-left
                                newboard[r-1][c-1] = 2
                                newboard[r][c] = 0
                                moves.append(newboard)
                                newboard = copy.deepcopy(board)
                            if c+1 < len(board):
                                if board[r-1][c+1] == 1: #move up-right
                                    newboard[r-1][c+1] = 2
                                    newboard[r][c] = 0
                                    moves.append(newboard)
                                    newboard = copy.deepcopy(board)
      
    return moves


## chooseBestMove function is based off a point system
    ## 1. difference between number of white vs. black pieces on the board
            ## points = points_t0
    ## 2. count the distance from either the very top( for black)
    ##    and from the very bottom (for white)
            ## points = points_t1
    ## 3. if the next move will cause the opponent to have no moves
            ## points = points_t2                                
 

def chooseBestMove(color, board):
    """
    This function chooses the best move out of a list of possible moves
    Parameter "color" is the color it is choosing moves for
    Parameter "board" is list of possible moves the color can make
    """
    points_total = 0
    max_board_index = 0
    points_t0 = []
    points_t12 = []

                #########################
    ### 1. counting number of white vs black pieces
                #########################
	
    for b in range(len(board)):
        whiteTotal = 0
        blackTotal = 0
        twhite = 0
        tblack = 0
        for r in range(len(board[b])):        
            white = board[b][r].count(1) # count amount of white pieces in each row
            black = board[b][r].count(2) # amount of black pieces in each row
            whiteTotal = whiteTotal + white
            blackTotal = blackTotal + black
            twhite = whiteTotal - blackTotal
            tblack = blackTotal - whiteTotal
                   
        if color == 1: #if evaluating for white
            points_t0.append(twhite)
        if color == 2: #evaluating for black
            points_t0.append(tblack)


                    #######################           
        ### 2. distance from opposite side of board
                    #######################
            
        ## simple point system:
	    ## distance = 0: wining => highest point 100
	    ## distance = 1: close to win => assign point 1
	    ## distance = others: hard to say

    for b in range(len(board)):
        points_t1 = 0   ## for #2
        points_t2 = 0   ## for #3
        for r in range(len(board[b])):
            for c in range(len(board[b][r])):
                distance = len(board[b])-1

                # calculating difference
                if color == 1:
                    if board[b][r][c] == 1: 
                        #subtract row positions #closer to row index len(board)
						## it's top down order, so we can use
                        distance = (len(board[b])-1) - r ## distance to bottom row

                if color == 2:
                    if board[b][r][c] == 2: 
                         #subtract row positions #closer to row index 0
				     ## it's bottom up order, so we can use
                        distance = r ## distance to top row = -(0-r)	
				
                if distance == 0: ## going to win, assign highest points
                    points_t1 = points_t1 + 100
                elif distance == 1:
                    points_t1 = points_t1 + 1 
                else:
                    points_t1 = points_t1 + 0							
                
		
                        #################################
	### 3. check to see if this move will cause the opponent to have no moves
                        #################################

        if points_t1 >= 100:
            points_t2 = 10
            
        else:
            if color == 1: #the player is white
                if generateMoves(1,board[b]) == []:
                    points_t2 = 100 
            if color == 2: #player is black
                if generateMoves(2,board[b]) == []:
                    points_t2 = 100

        points_t12.append(points_t1 + points_t2)

                ####################	
    ## choosing the board with the largest point value
                ####################
 
    max_num = 0
    for b in range(len(board)):
        points_total = points_t0[b] + points_t12[b] 
        if points_total > max_num:
            max_num = points_total
            max_board_index = b
    return board[max_board_index]



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




