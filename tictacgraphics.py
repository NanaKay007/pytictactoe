from graphics import *
from random import choice

def displayboard(board,window,gridX,gridY,points_list):
    """
    Draws the square board based on user's choice
    writes all square coordinates to a list
    parameters: window
    return: none
    """
    #draws the square board
    for i in range(gridX):
        for j in range(gridY):
            corner1 = Point(50*(j+1),50*(i+1))
            corner2 = Point(100 + (50*(j)),100 + (50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)

    #maps each square to a slot on the board
    for i in range(len(board)):
        map_dict[i] = points_list[i]

def drawAiChoice(board,window,ai_choice,points_list):
    """
    draws the symbol '0' for the AI
    parameters: board,window
    """
    square_coords = points_list[ai_choice]
    board[ai_choice] = '0'

    x_1 = square_coords[0].getX()
    y_1 = square_coords[0].getY()

    x_2 = square_coords[1].getX()
    y_2 = square_coords[1].getY()

    anchor_x = (x_1 + x_2)/2
    anchor_y = (y_1 + y_2)/2

    O = Text(Point(anchor_x,anchor_y),'0')
    O.draw(window)

    return 0

def getUserChoice(window,points_list,board):
    """
    draws an X (for the user) in the square board.
    parameters : window
    """
    clickPoint = window.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()

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
        elif (x > x_1 and x < x_2 and y > y_1 and y < y_2 ) and board[point_index] != ' ':
            print('invalid input')

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))
    board = list(' '*(user_gridX_choice*user_gridY_choice))
    closeWindow = False
    points_list = []

    #constructs the window
    x = 1000
    y = 800
    window = GraphWin("Welcome To TicTacToe!",x,y)
    window.setBackground('white')

    #constructs the board and the input UI
    displayboard(board,window,user_gridX_choice,user_gridY_choice,points_list)

    #testing draw0
    ai_choice = choice([1,2,3])

    while closeWindow == False:
        getUserChoice(window,points_list,board)
        drawAiChoice(board,window,ai_choice,points_list)
        print(board)
    window.getMouse()
    window.close()

main()
