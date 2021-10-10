"""
6.

"""

import random



#******************************
def check_danger():
    global danger

    flag_danger = 0
    rowWQ = white_queen // stiles
    colWQ = white_queen % stiles

    start_row = rowWQ
    start_col = colWQ

    rowBO = black_officer // stiles
    colBO = black_officer % stiles

    
    # diagonal 1
    start_row = rowWQ
    start_col = colWQ
    if flag_danger == 0:
        if colWQ == 0:
            start_row = rowWQ
            start_col = colWQ
        else:
            flag1 = 1
            while flag1:
                if start_row - 1 >= 0 and start_col - 1 >= 0:
                    start_row -= 1
                    start_col -= 1
                else:
                    flag1 = 0


        flag1 = 1
        while flag1:
            if (start_row == rowBO) and (start_col == colBO):
                flag_danger = 1
                flag1 = 0
            else:
                start_row += 1
                start_col += 1 
                if start_row > 7 or start_col > 7:
                    flag1 = 0

    # diagonal 2
    start_row = rowWQ
    start_col = colWQ
    if flag_danger == 0:
        if rowWQ == 0:
            start_row = rowWQ
            start_col = colWQ
        else:
            flag1 = 1
            while flag1:
                if start_row - 1 >= 0 and start_col + 1 <= 7:
                    start_row -= 1
                    start_col += 1
                else:
                    flag1 = 0

        flag1 = 1
        while flag1:
            if (start_row == rowBO) and (start_col == colBO):
                flag_danger = 1
                flag1 = 0
            else:
                start_row += 1
                start_col -= 1 
                if start_row > 7 or start_col < 0:
                    flag1 = 0
    
    if flag_danger == 1:
        danger += 1
        # for row in range(grames):
        #     print(board[row])
        # print()


    return 
#******************************

danger = 0 


stiles = 8
grames = stiles



for times in range(100):

    board = [] # skakiera

    theseis = (grames * stiles)
    
    for i in range(grames):
        L1 = []
        for j in range(stiles):
            L1.append("00")
        board.append(L1)

    white_queen = random.randint(0,theseis-1)
    row = white_queen // stiles
    col = white_queen % stiles
    board[row][col] = "WQ" 


    i=1
    while i :
        black_officer = random.randint(0,theseis-1)
        row = black_officer // stiles
        col = black_officer % stiles
        if board[row][col] == "00":
            board[row][col] = "BO"
            i=0        
        
    
    # for row in range(grames):
    #     print(board[row])
    # print()
    

    
    check_danger()


print( 'σε απειλή      : ', danger )   
  
