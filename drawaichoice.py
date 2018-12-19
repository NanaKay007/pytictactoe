from graphics import *

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
