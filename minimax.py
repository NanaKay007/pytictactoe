from emptyslotchecker import emptySlotChecker
from checkwinner import isWinner

def minimax(board,gridX,gridY):
    best_move_ai = {'move':[],'score': 0}
    alpha = 0
    beta = 0
    inf = float('inf')

    def max_value(board,alpha,beta):
        #empty slots
        allowed_moves = emptySlotChecker(board)
        aiplayer = '0'
        humplayer = 'X'
        ai_win_check = isWinner(board,aiplayer,gridX,gridY)
        human_win_check = isWinner(board,humplayer,gridX,gridY)
        if  ai_win_check[1]== True:
            best_move_ai['move'].append(ai_win_check[0])
            best_move_ai['score'] = 10
            return best_move_ai['score']
        elif human_win_check[1] == True:
            best_move_ai['move'].append(human_win_check[0])
            best_move_ai['score'] = -10
            return best_move_ai['score']
        else:
            if len(allowed_moves) == 0:
                best_move_ai['move'].append(board)
                best_move_ai['score'] = 0
                return best_move_ai['score']

        total_score = -inf
        for a in allowed_moves:
            board[a] = aiplayer
            new_score = max(total_score,min_value(board,alpha,beta))
            total_score = new_score
            print(board)
            board[a] = ' '
            if total_score >= beta:
                return total_score
            alpha = max(alpha,total_score)
        return total_score

    def min_value(board,alpha,beta):
        humplayer = 'X'
        aiplayer = '0'
        ai_win_check = isWinner(board,aiplayer,gridX,gridY)
        human_win_check = isWinner(board,humplayer,gridX,gridY)
        allowed_moves = emptySlotChecker(board)
        if human_win_check[1] == True:
            best_move_ai['move'].append(human_win_check[0])
            best_move_ai['score'] = -10
            return best_move_ai[1]
        elif ai_win_check[1] == True:
            best_move_ai['move'].append(ai_win_check[0])
            best_move_ai['score'] = 10
            return best_move_ai['score']
        else:
            if len(allowed_moves) == 0:
                best_move_ai['move'].append(board)
                best_move_ai['score'] = 0
                return best_move_ai['score']

        total_score = inf
        for a in allowed_moves:
            board[a] = humplayer
            new_score = min(total_score,max_value(board,alpha,beta))
            total_score = new_score
            print(board)
            board[a] = ' '
            if total_score<= alpha:
                return total_score
            beta = min(beta,total_score)
        return total_score

    max_value(board,alpha,beta)
    print(best_move_ai)
    return best_move_ai
