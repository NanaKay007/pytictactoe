"""
Implements a tic-tac-toe game with two players: a user and an AI
Author: Anikuabe Nana Kweku
"""
import random
from graphics import *

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

def displayBoard(board,window,gridX,gridY,points_list):
    """
    Draws the square board based on user's choice
    writes all square coordinates to a list
    parameters: window
    return: none
    """
    #draws the square board

    for i in range(gridX):
        for j in range(gridY):
            corner1 = Point(50+(50*j),100+(50*i))
            corner2 = Point(100+(50*(j)),150+(50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)

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

def aiTurn(board,window,gridX,gridY,points_list):
    #keeps track of the empty slots in the board
    empty_slot_list = emptySlotChecker(board)

    #returns the best_move object
    choice = minimax(board,gridX,gridY)

    #isolates the moves board from the best_move object
    best_move_board = choice['move']

    """decides the AI's choice if a terminal state results in
    the AI winning
    """
    if len(choice['move']) != 0 and (choice['score'] == 10 or choice['score'] == 0):
        #loops through the indices in the moves_board
        for move_index in range(len(best_move_board)):
            if best_move_board[move_index] == '0' and (move_index in empty_slot_list):
                board[move_index] = '0'
                print('AI chooses: ',move_index)
                drawAiChoice(board,window,move_index,points_list)
                break
    elif len(choice['move']) != 0 and choice['score'] == -10:
        """decides the AI's choice if a terminal state results in
        the AI losing
        """
        for move_index in range(len(best_move_board)):
            if best_move_board[move_index] == 'X' and (move_index in empty_slot_list):
                board[move_index] = '0'
                print('AI chooses: ',move_index)
                drawAiChoice(board,window,move_index,points_list)
                break
    else:
        move_index = random.choice(empty_slot_list)
        board[move_index] = '0'
        drawAiChoice(board,window,move_index,points_list)

def drawAiChoice(board,window,ai_choice,points_list):
    """
    draws the symbol '0' for the AI
    parameters: board,window
    """
    square_coords = points_list[ai_choice]

    x_1 = square_coords[0].getX()
    y_1 = square_coords[0].getY()

    x_2 = square_coords[1].getX()
    y_2 = square_coords[1].getY()

    anchor_x = (x_1 + x_2)/2
    anchor_y = (y_1 + y_2)/2

    O = Text(Point(anchor_x,anchor_y),'0')
    O.draw(window)

def minimax(board,gridX,gridY):
    best_move_ai = {'move':'','score': 0}
    alpha = 0
    beta = 0
    def max_value(board,alpha,beta):
        #empty slots
        allowed_moves = emptySlotChecker(board)
        new_board = board.copy()
        aiplayer = '0'
        if isWinner(new_board,aiplayer,gridX,gridY) == True:
            best_move_ai['move'] = new_board
            best_move_ai['score'] = 10
            return best_move_ai['score']
        total_score = -1000
        for a in allowed_moves:
            new_board_2 = new_board.copy()
            new_board_2[a] = aiplayer
            new_score = max(total_score,min_value(new_board_2,alpha,beta))
            total_score = new_score
            if total_score >= beta:
                return total_score
            alpha = max(alpha,total_score)
        return total_score

    def min_value(board,alpha,beta):
        humplayer = 'X'
        new_board = board.copy()
        allowed_moves = emptySlotChecker(board)
        if isWinner(new_board,humplayer,gridX,gridY) == True:
            best_move_ai['move'] = new_board
            best_move_ai['score'] = -10
            return best_move_ai['score']
        total_score = 1000
        for a in allowed_moves:
            new_board_2 = new_board.copy()
            new_board_2[a] = humplayer
            new_score = min(total_score,max_value(new_board_2,alpha,beta))
            total_score = new_score
            if total_score<= alpha:
                return total_score
            beta = min(beta,total_score)
        return total_score

    min_value(board,alpha,beta)
    max_value(board,alpha,beta)
    print(best_move_ai)
    return best_move_ai

def getUserChoice(window,points_list,board,quit):
    """
    draws an X (for the user) in the square board or closes game
    parameters : window
    """
    #user click Point
    clickPoint = window.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()

    #quit button anchor points
    corner_1 = quit.getP1()
    corner_2 = quit.getP2()

    cx_1 = corner_1.getX()
    cy_1 = corner_1.getY()

    cx_2 = corner_2.getX()
    cy_2 = corner_2.getY()

    for (point1,point2) in points_list:
        #keeps the index of a point object
        point_index = points_list.index((point1,point2))
        x_1 = point1.getX()
        y_1 = point1.getY()

        x_2 = point2.getX()
        y_2 = point2.getY()

        #checks wether the coordinates of a clickpoint exists within the confines of a square
        #if the square is empty, it draws an X and updates the board object
        if (x > x_1 and x < x_2 and y > y_1 and y < y_2 ) and board[point_index] == ' ':
            anchor_x = (x_1 + x_2)/2
            anchor_y = (y_1 + y_2)/2
            X = Text(Point(anchor_x,anchor_y),'X')
            X.draw(window)
            board[point_index] = 'X'
            return False
        #condition to check when the user clicks an occupied point
        elif (x > x_1 and x < x_2 and y > y_1 and y < y_2 ) and board[point_index] != ' ':
            print('invalid input')
        elif (x < cx_2 and x > cx_1) and (y < cy_2 and y > cy_1):
            window.close()

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
        if win_count == gridX:
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
        win_count = slot_list_2.count(symbol)
        if win_count == gridX:
            isWinner_bool = True

    return isWinner_bool

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))

    #welcome section
    # sample_board = list(range(user_gridX_choice * user_gridY_choice))
    # welcome_text(sample_board,user_gridX_choice,user_gridY_choice)

    #main program
    board = list(" "*(user_gridX_choice*user_gridY_choice))
    isGameOver = False
    num_empty_slots = len(emptySlotChecker(board))
    points_list = []

    #constructs the window
    square_length = 50

    board_width = square_length * user_gridX_choice
    board_height = square_length * user_gridY_choice

    window_x = 50 + board_width + 50
    window_y = 100 + board_height + 150

    window = GraphWin("Welcome To TicTacToe!",window_x,window_y)
    window.setBackground('white')

    #draws the header
    anchor_point = Point(window_x/2,50)
    header = Text(anchor_point,'Welcome to Tic-Tac-Smart!')
    header.draw(window)
    
    #draws the quit button
    quit_center = Point(window_x/2,window_y-50)
    quit_button_text = Text(quit_center,'Quit')
    quit_box_corner_1 = Point(quit_center.getX()-20,quit_center.getY()-20)
    quit_box_corner_2 = Point(quit_center.getX()+20,quit_center.getY()+20)
    quit_button_border = Rectangle(quit_box_corner_1,quit_box_corner_2)
    quit_button_border.draw(window)
    quit_button_text.draw(window)

    displayBoard(board,window,user_gridX_choice,user_gridY_choice,points_list)
    while isGameOver == False:
        if num_empty_slots != 0:
            print()
            aiTurn(board,window,user_gridX_choice,user_gridY_choice,points_list)
            num_empty_slots -= 1
            isGameOver = isWinner(board,'0',user_gridX_choice,user_gridY_choice)
            # displayBoard(board,window,user_gridX_choice,user_gridY_choice,points_list)
            if num_empty_slots != 0:
                if isGameOver == False:
                    # userTurn(board)
                    isGameOver = getUserChoice(window,points_list,board,quit_button_border)
                    num_empty_slots -=1
                    isGameOver = isWinner(board,'X',user_gridX_choice,user_gridY_choice)
                    # displayBoard(board,user_gridX_choice,user_gridY_choice)
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
    
    window.getMouse()
    window.close()

main()
