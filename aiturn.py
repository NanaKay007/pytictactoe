from graphics import *
from emptyslotchecker import emptySlotChecker
from checkwinner import isWinner
from minimax import minimax
from drawaichoice import drawAiChoice
import random

def aiTurn(board,window,gridX,gridY,points_list):
    #keeps track of the empty slots in the board
    empty_slot_list = emptySlotChecker(board)

    #returns the best_move object
    choice = minimax(board,gridX,gridY)

    #isolates the moves board from the best_move object
    best_move_board = choice['move']
    print("best move is ",best_move_board)
    """decides the AI's choice if a terminal state results in
    the AI winning
    """
    if len(choice['move']) != 0 and (choice['score'] == 10):
        #loops through the indices in the moves_board
        print("when move board is not 0 and score is 0 or 10")
        for move in best_move_board:
            if move in empty_slot_list:
                board[move] = '0'
                print('I played ',move)
                drawAiChoice(board,window,move,points_list)
                return
            else:
                move_index = random.choice(empty_slot_list)
                board[move_index] = '0'
                print(" I randomly chose ",move_index)
                drawAiChoice(board,window,move_index,points_list)
                return
    elif choice['score'] == 0:
        for move in best_move_board:
            if move == '0' and best_move_board.index(move) in empty_slot_list:
                board[best_move_board.index(move)] = '0'
                print('I played ',move)
                drawAiChoice(board,window,move,points_list)
                return
            else:
                move_index = random.choice(empty_slot_list)
                board[move_index] = '0'
                print(" I randomly chose ",move_index)
                drawAiChoice(board,window,move_index,points_list)
                return
    elif len(choice['move']) != 0 and choice['score'] == -10:
        """decides the AI's choice if a terminal state results in
        the AI losing
        """
        print("when move board isnt zero and choice is -10...")
        for move in best_move_board:
            if move in empty_slot_list:
                print("I put ",move)
                board[move] = '0'
                drawAiChoice(board,window,move,points_list)
                return
            else:
                move_index = random.choice(empty_slot_list)
                board[move_index] = '0'
                print(" I randomly chose ",move_index)
                drawAiChoice(board,window,move_index,points_list)
                return
    else:
        move_index = random.choice(empty_slot_list)
        board[move_index] = '0'
        print(" I randomly chose ",move_index)
        drawAiChoice(board,window,move_index,points_list)
        return
