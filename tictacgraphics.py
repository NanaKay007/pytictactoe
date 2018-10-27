from graphics import *

def displayboard(window,gridX,gridY,points_list):
    """
    Draws the square board based on user's choice
    writes all square coordinates to a list
    parameters: window
    return: none
    """
    for i in range(gridX):
        for j in range(gridY):
            corner1 = Point(50*(j+1),50*(i+1))
            corner2 = Point(50 + (50*(j)),100 + (50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)

def drawX(window):
    """
    draws an X (for the user) in the square board.
    parameters : window 
    """




def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))
    
    #constructs the window
    x = 1000
    y = 800
    window = GraphWin("Welcome To TicTacToe!",x,y)
    window.setBackground('white')

    #constructs the board and the input UI
    points_list = []
    displayboard(window,user_gridX_choice,user_gridY_choice,points_list)
    print(points_list)
    window.getMouse()
    window.close()

main()
