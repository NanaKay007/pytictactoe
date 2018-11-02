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
            corner1 = Point(50+(50*j),100+(50*i))
            corner2 = Point(100+(50*(j)),150+(50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)

    #maps each square to a slot on the board
    # for i in range(len(board)):
    #     map_dict[i] = points_list[i]

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

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))
    board = list(' '*(user_gridX_choice*user_gridY_choice))
    closeWindow = False
    points_list = []

    #constructs the window
    square_length = 50

    board_width = square_length * user_gridX_choice
    board_height = square_length * user_gridY_choice

    window_x = 50 + board_width + 50
    window_y = 100 + board_height + 150

    window = GraphWin("Welcome To TicTacToe!",window_x,window_y)
    window.setBackground('white')

    #draws the quit button
    quit_center = Point(window_x/2,window_y-50)
    quit_button_text = Text(quit_center,'Quit')
    quit_box_corner_1 = Point(quit_center.getX()-20,quit_center.getY()-20)
    quit_box_corner_2 = Point(quit_center.getX()+20,quit_center.getY()+20)
    quit_button_border = Rectangle(quit_box_corner_1,quit_box_corner_2)
    quit_button_border.draw(window)
    quit_button_text.draw(window)

    #constructs the board and the input UI
    displayboard(board,window,user_gridX_choice,user_gridY_choice,points_list)

    #testing draw0
    ai_choice = choice([1,2,3])

    while closeWindow == False:
        closeWindow = getUserChoice(window,points_list,board,quit_button_border)
        if closeWindow == False:
            drawAiChoice(board,window,ai_choice,points_list)

main()
