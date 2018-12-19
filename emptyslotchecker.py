def emptySlotChecker(board):
    """
    keeps an updated list of empty slots on the board
    during the course of the game
    parameter: board
    """
    empty_slots =[]
    board_indices = list(range(len(board)))
    for i in board_indices:
        if board[i] == ' ':
            empty_slots.append(i)
    return empty_slots
