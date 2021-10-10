"""
1.
"""

import random

#******************************
def ckeck_wrong_position():
    global wrong_position

    flag = 0
    rowWK = white_king // stiles
    colWK = white_king % stiles
    
    L=[]
    if rowWK - 1 >= 0:
        L.append([rowWK-1,colWK])
        if colWK - 1 >=0:
            L.append([rowWK-1,colWK-1])
        if colWK + 1 < 8 :
            L.append([rowWK-1,colWK+1])

    if colWK - 1 >=0:
        L.append([rowWK,colWK-1])
    if colWK + 1 < 8 :        
        L.append([rowWK,colWK+1])

    if rowWK + 1 <8:
        L.append([rowWK+1,colWK])
        if colWK - 1 >=0:
            L.append([rowWK+1,colWK-1])
        if colWK + 1 < 8 :
            L.append([rowWK+1,colWK+1])

    i=0
    while i < len(L):
        if board[L[i][0]][L[i][1]] == "BK":
            flag = 1
            wrong_position += 1
            i=len(L)
            # for row in range(grames):
            #     print(board[row])
            # print()

        i+=1


    return flag
#******************************

#******************************
def check_danger():
    global danger

    flag_danger = 0
    rowWQ = white_queen // stiles
    colWQ = white_queen % stiles

    start_row = rowWQ
    start_col = colWQ

    rowBK = black_king // stiles
    colBK = black_king % stiles

    # horizontal or vertical
    if (rowBK == rowWQ) or (colBK == colWQ):
        flag_danger = 1

    
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
            if (start_row == rowBK) and (start_col == colBK):
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
            if (start_row == rowBK) and (start_col == colBK):
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
wrong_position = 0

stiles = 8
grames = stiles
flag = 0


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
        white_king = random.randint(0,theseis-1)
        row = white_king // stiles
        col = white_king % stiles
        if board[row][col] == "00":
            board[row][col] = "WK"
            i=0

    i=1
    while i :
        black_king = random.randint(0,theseis-1)
        row = black_king // stiles
        col = black_king % stiles
        if board[row][col] == "00":
            board[row][col] = "BK"
            i=0        
        
    
    # for row in range(grames):
    #     print(board[row])
    # print()
    

    flag = ckeck_wrong_position()
    if flag == 0:
        check_danger()


print( 'σε απειλή      : ', danger )   
print( 'σε λάθος θέση  : ', wrong_position )   
