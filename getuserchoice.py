from graphics import *

def getUserChoice(window,points_list,board):
    """
    draws an X (for the user) in the square board or closes game
    parameters : window
    """
    #user click Point
    clickPoint = window.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()

    # #quit button anchor points
    # corner_1 = quit.getP1()
    # corner_2 = quit.getP2()
    #
    # cx_1 = corner_1.getX()
    # cy_1 = corner_1.getY()
    #
    # cx_2 = corner_2.getX()
    # cy_2 = corner_2.getY()

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
        # elif (x < cx_2 and x > cx_1) and (y < cy_2 and y > cy_1):
        #     window.close()
