def isWinner(board,symbol,gridX,gridY):
    """
    checks the winner while empty slots are available;
    ends game if there are no slots
    parameters: board, symbol
    """
    winning_set = [[],False]

    for i in range(gridX):
        #checks columns for a winner
        col_indx = list(range(i,gridX*gridY,gridX))
        slot_list = []
        for i in col_indx:
            slot_list.append(board[i])
        win_count = slot_list.count(symbol)
        if win_count == gridY:
            winning_set[1] = True
            for i in col_indx:
                winning_set[0].append(i)
    #checks rows
    for i in range(0,gridX*gridY,gridX):
        row_indx = list(range(i,i+gridX))
        slot_list = []
        for i in row_indx:
            slot_list.append(board[i])
        win_count = slot_list.count(symbol)
        if win_count == gridX:
            winning_set[1] = True
            for i in row_indx:
                winning_set[0].append(i)


    #checks diagonals for a winner if the board is symmetric
    if gridX == gridY:
        #checks left diagonal
        diag_count_1 = 0
        slot_list_1 = []
        diag_indx = list(range(0,gridX*gridY,gridX))
        for i in diag_indx:
            slot_list_1.append(board[i+diag_count_1])
            diag_count_1 += 1
        win_count = slot_list_1.count(symbol)
        if win_count == gridX:
            winning_set[1] = True
            for i in diag_indx:
                winning_set[0].append(i)


        #checks right diagonal
        diag_count_2 = gridY-1
        slot_list_2 = []
        diag_indx_2 = list(range(0,gridX*gridY,gridX))
        for i in diag_indx_2:
            slot_list_2.append(board[i+diag_count_2])
            diag_count_2 -= 1
        win_count = slot_list_2.count(symbol)
        if win_count == gridX:
            winning_set[1] = True
            for i in diag_indx:
                winning_set[0].append(i)
    return winning_set
