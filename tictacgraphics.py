from graphics import *

def displayboard(window,gridX,gridY):
    """
    Draws the square board based on user's choice
    parameters: window
    return: none
    """
    for i in range(gridX):
        for j in range(gridY):
            corner1 = Point(50*(j+1),50*(i+1))
            corner2 = Point(100 + (50*(j)),100 + (50*(i)))
            square = Rectangle(corner1,corner2)
            square.draw(window)



    # square.draw(window)
    return 0

def displayinput(window):
    """
    Displays the UI for entering a choice
    parameters: window
    return: input_text
    """
    # text_input = Entry(Point(300,300),10)
    text_str = Text(Point(300,400),"hello")
    # text_input.draw(window)
    # text_str.draw(window)
    #
    # choice = text_input.getText() #extracts input text
    # window.getMouse()
    # text_str.setText(choice)
    # text_str.draw(window)

    checkPoint = window.checkMouse()
    while checkPoint != None:
        
        checkPoint.draw(window)
    else:
        text_str.draw(window)
    return 0


def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))
    #constructs the window
    window = GraphWin("Welcome To TicTacToe!",600,600)
    #constructs the board and the input UI
    displayboard(window,user_gridX_choice,user_gridY_choice)
    displayinput(window)
    window.getMouse()
    window.close()





main()
