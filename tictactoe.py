"""
Implements a tic-tac-toe game with two players: a user and an AI
Author: Anikuabe Nana Kweku
"""
import random
from graphics import *
from displayboard import displayBoard
from aiturn import aiTurn
from drawaichoice import drawAiChoice
from minimax import minimax
from getuserchoice import getUserChoice
from checkwinner import isWinner
from emptyslotchecker import emptySlotChecker

def main():
    user_gridX_choice = int(input('Please enter grid dimension X: '))
    user_gridY_choice = int(input('Please enter grid dimesion Y: '))

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
            aiTurn(board,window,user_gridX_choice,user_gridY_choice,points_list)
            num_empty_slots -= 1
            ai_check = isWinner(board,'0',user_gridX_choice,user_gridY_choice)
            isGameOver = ai_check[1]
            if num_empty_slots != 0:
                if isGameOver == False:
                    isGameOver = getUserChoice(window,points_list,board,quit_button_border)
                    num_empty_slots -=1
                    user_check = isWinner(board,'X',user_gridX_choice,user_gridY_choice)
                    isGameOver = user_check[1]
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
