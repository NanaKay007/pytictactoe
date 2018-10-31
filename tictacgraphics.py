from graphics import *

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
            corner1 = Point(300*(j+1),50*(i+1))
            corner2 = Point(350 + (50*(j)),100 + (50*(i)))
            points_list.append((corner1,corner2))
            square = Rectangle(corner1,corner2)
            square.draw(window)

    map_dict = {}
    #maps each square to a slot on the board
    for i in range(len(board)):
        map_dict[board[i]] = points_list[i]




def drawX(window,points_list):
    """
    draws an X (for the user) in the square board.
    parameters : window
    """
    clickPoint = window.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()

    for (point1,point2) in points_list:
        x_1 = point1.getX()
        y_1 = point1.getY()

        x_2 = point2.getX()
        y_2 = point2.getY()

        if (x > x_1 and x < x_2 and y > y_1 and y < y_2  ):
            anchor_x = (x_1 + x_2)/2
            anchor_y = (y_1 + y_2)/2
            X = Text(Point(anchor_x,anchor_y),'X')
            X.draw(window)

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))
    board = list(range(user_gridX_choice*user_gridY_choice))
    closeWindow = False
    points_list = []
    #constructs the window
    x = 1000
    y = 800
    window = GraphWin("Welcome To TicTacToe!",x,y)
    window.setBackground('white')

    #constructs the board and the input UI
    displayboard(board,window,user_gridX_choice,user_gridY_choice,points_list)
    while closeWindow == False:
        drawX(window,points_list)
    window.getMouse()
    window.close()

main()
