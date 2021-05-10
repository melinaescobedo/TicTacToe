#--------- TIC TAC TOE ---------#

# Initialize the board to be empty in all the positions
# Player inputs would be entered in the position he choose
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Print out the board
def printBoard(board):
    print('\n')
    print(' ', board[1], '|', board[2], '|', board[3], ' ')
    print('-------------')
    print(' ', board[4], '|', board[5], '|', board[6], ' ')
    print('-------------')
    print(' ', board[7], '|', board[8], '|', board[9], ' ')
    print('\n')

# printBoard(board)

# Check if the space is free
def freeSpace(position):
    # If the space is empty return True and if the space is occupied return False
    if(board[position] == ' '):
        return True
    else:
        return False

# Check if the game has no solution 'State Toe'
def checkTie():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

#Check the diagonals, columns and rows to verify if one player has won
def checkWinner():
    if   (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# Used to find the terminal state to exit the recursion
# Here we know which player has won
def checkMark(mark):
    if   (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

#Check if there is a winner or if the game is tied and announce it to the player
def inputInserted(inputIn, position):
    if freeSpace(position):
        board[position] = inputIn
        printBoard(board)

        if checkTie():
            print("Ups! You got Tie :(")
            # print("The game got cajoled!")
            exit()

        if checkWinner():
            if inputIn == '0':
                print("The AI wins!")
                # print("Jupi! 2nd Player won this round")
                exit()
            else:
                print("Good job, you win!")
                # print("Wuuuu 1st Player won this round!")
                exit()
        return
    
    else:
        print("This position in not available, insert another one!")
        position = int(input("New position: "))
        inputInserted(inputIn, position)
        return

# Moves that each player should do and the AI moves 

player = 'X'
# player2 = '0'
AI = '0'

# Manual Player 1
def pMove():
    position = int(input("Enter 'X' position: "))
    inputInserted(player, position)
    return

# Manual Player 2
''' 
def p2Move():
    position = int(input("Enter '0' position: "))
    inputInserted(player2, position)
    return 
'''

# AI Player
def aIMove():
    bestScore = -999     # Begin with the low score
    bestMove = 0

    for key in board.keys():    # Go through each possible position
        if(board[key] == ' '):  # If each board key is equal to an empty space the AI is goin to use it
            board[key] = AI
            score = minimax(board, 0, False)    # Determine the score
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key

    inputInserted(AI, bestMove) # Insert the best move that we found previously
    return

# Minimax Algorithm
# This AI will consider all possible scenarios and makes the most optimal move
# This function evaluates all the available moves using minimax() and then returns the best move the maximizer can make
# This algorithm will check every possible position, assigns scores to each one and choose the one with the best score, in other words the code goes recursively to each possible position and picks the best move to afford a win or to draw or tie the game so that the player does not win
def minimax(board, depth, maximizingTree):  # Maximazing | Depth is used in more complicated cases, in wich we need to stop in a specific or certain depth because there can be a lot of moves, but here we just have nine moves, so we can ignore it or just don't write it
    if checkMark(AI):
        return 1

    elif checkMark(player):
        return -1

    elif checkTie():
        return 0

# AI
    if maximizingTree:  # Determine which player is playing
        bestScore = -999

        for key in board.keys():
            if(board[key] == ' '):
                board[key] = AI
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score

        return bestScore
        
# Enemy AI
    else:
        bestScore = 999
        for key in board.keys():
                if(board[key] == ' '):
                    board[key] = player
                    score = minimax(board, depth + 1, True)
                    board[key] = ' '
                    if(score < bestScore):
                       bestScore = score

        return bestScore

while not checkWinner():
    pMove()
    # p2Move()
    aIMove()
