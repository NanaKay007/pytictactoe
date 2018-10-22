"""
Implements a tic-tac-toe game with two players: a user and an AI
Author: Anikuabe Nana Kweku
"""
import random

def welcome_text(board,gridX,gridY):
    welcome_text = 'Welcome to Tic-Tac-Toe!'
    print('*' * len(welcome_text))
    print(welcome_text)
    print('*' * len(welcome_text))
    print()
    print('Enter your choice like the numbers below:')
    print()
    displayBoard(board,gridX,gridY)
    print()

def displayBoard(board,gridX,gridY):
    print('-' * gridX)
    accum = '|'
    #checks the length each number should have
    max_int = str(len(board))
    max_length = 0
    for i in max_int:
        max_length+=1

    #formats each number to be uniform and have the pipe character
    slot_list = []
    space = ' '
    pipe = '|'
    for i in board:
        num = str(i)
        if len(num) < max_length:
            new_numstr = num + (space * (max_length - len(num))+ pipe)
            slot_list.append(new_numstr)
        else:
            slot_list.append(num+pipe)

    #prints the rows of the sample board
    for i in range(0,len(board),gridX):
        row = slot_list[i:i+gridX]
        board_row = '|'
        for i in row:
            board_row += i
        print(board_row)

    print('-'*gridX)

def emptySlotChecker(board):
    """
    keeps an updated list of empty slots on the board
    during the course of the game
    parameter: board
    """
    empty_slots =[]
    board_indices = list(range(len(board)))
    for i in board_indices:
        if board[i] == ' ':
            empty_slots.append(i)
    return empty_slots

def aiTurn(board):
    #keeps track of the empty slots in the board
    empty_slot_list = emptySlotChecker(board)
    #makes a choice randomly
    choice = random.choice(empty_slot_list)
    print('AI chooses: ',choice)
    board[choice] = '0'

def userTurn(board):
    """
    allows user to input a choice and checks wether the choice
    is valid.
    parameter: board
    """
    #keeps track of empty slots in the board
    empty_slot_list = emptySlotChecker(board)

    #asks and checks that the user input is valid and not taken
    user_choice = int(input('Enter 0-8 for your choice: '))
    while not(user_choice in empty_slot_list):
        print("Invalid input: %s" % user_choice)
        user_choice = int(input('Enter 0-8 for your choice: '))
    else:
        board[user_choice] = 'X'

def isWinner(board,symbol,gridX,gridY):
    """
    checks the winner while empty slots are available;
    ends game if there are no slots
    parameters: board, symbol
    """
    isWinner_bool = False
    for i in range(gridX):
        #checks columns for a winner
        col_indx = list(range(i,gridX*gridY,gridX))
        slot_list = []
        for i in col_indx:
            slot_list.append(board[i])
        win_count = slot_list.count(symbol)
        if win_count == gridY:
            isWinner_bool = True

    #checks rows
    for i in range(0,gridX*gridY,gridX):
        row_indx = list(range(i,i+gridX))
        slot_list = []
        for i in row_indx:
            slot_list.append(board[i])
        win_count = slot_list.count(symbol)
        if win_count == gridY:
            isWinner_bool = True

    #checks diagonals for a winner if the board is symmetric
    if gridX == gridY:
        #checks left diagonal
        diag_count_1 = 0
        slot_list_1 = []
        for i in range(0,gridX*gridY,gridX):
            slot_list_1.append(board[i+diag_count_1])
            diag_count_1 += 1
        win_count = slot_list_1.count(symbol)
        if win_count == gridX:
            isWinner_bool = True

        #checks right diagonal
        diag_count_2 = gridY-1
        slot_list_2 = []
        for i in range(0,gridX*gridY,gridX):
            slot_list_2.append(board[i+diag_count_2])
            diag_count_2 -= 1
        print(slot_list_2)
        win_count = slot_list_2.count(symbol)
        if win_count == gridX:
            isWinner_bool = True

    return isWinner_bool

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))

    #welcome section
    sample_board = list(range(user_gridX_choice * user_gridY_choice))
    welcome_text(sample_board,user_gridX_choice,user_gridY_choice)

    #main program
    random.seed(2)
    board = list(" "*(user_gridX_choice*user_gridY_choice))
    isGameOver = False
    num_empty_slots = len(emptySlotChecker(board))

    while isGameOver == False:
        if num_empty_slots != 0:
            print()
            aiTurn(board)
            print(isGameOver)
            num_empty_slots -= 1
            isGameOver = isWinner(board,'0',user_gridX_choice,user_gridY_choice)
            displayBoard(board,user_gridX_choice,user_gridY_choice)
            if num_empty_slots != 0:
                if isGameOver == False:
                    userTurn(board)
                    num_empty_slots -=1
                    isGameOver = isWinner(board,'X',user_gridX_choice,user_gridY_choice)
                    print(isGameOver)
                    displayBoard(board,user_gridX_choice,user_gridY_choice)
                    if isGameOver == True:
                        print('User Wins!')
                else:
                    print('AI wins!')
            else:
                isGameOver = True
        else:
            isGameOver = True
    else:
        if num_empty_slots == 0:
            print('It\'s a draw')
        print('Game Over')
main()
