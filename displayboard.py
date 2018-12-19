
from graphics import *

def displayBoard(board,window,gridX,gridY,points_list):
    """
    Draws the square board based on user's choice
    writes all square coordinates to a list
    parameters: window
    return: none
    """
    #draws the square board

    for i in range(gridY):
        for j in range(gridX):
            corner1 = Point(50+(50*j),100+(50*i))
            corner2 = Point(100+(50*(j)),150+(50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)
