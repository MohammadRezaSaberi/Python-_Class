def show_boardgame(board_game):
    print()

    for i in range(3):
        for j in range(3):
            print(board_game[i][j], end=' ')
        print()

    print() 

board_game = [['_ ', '_ ', '_ '],
              ['_ ', '_ ', '_ '],
              ['_ ', '_ ', '_ ']]       
show_boardgame(board_game)

while True :
    #X
    while True : 
        player1_row = int(input(' (X) Which Row? '))
        player1_column = int(input(' (X) Which column? '))

        # Check Input Range
        if (1 <= player1_row <=3 ) and ( 1 <= player1_column <=3 ) :
            pass
        else :
            print('(X) Wrong Input! Please Try Again. ')
            continue

        # Check box is empty or is not empty
        if board_game[player1_row - 1 ][player1_column - 1 ] == '_ ' :
            board_game[player1_row - 1 ][player1_column - 1] = 'X'
            break
        else : 
            print('(X) This box is not empty! Please Try Again. ')

    show_boardgame(board_game)   

    #o
    while True : 
        player2_row = int(input(' (O) Which Row? '))
        player2_column = int(input(' (O) Which column? '))

        # Check Input Range
        if (1 <= player2_row <=3 ) and ( 1 <= player2_column <=3 ) :
            pass
        else :
            print('(O) Wrong Input! Please Try Again. ')
            continue

        # Check box is empty or is not empty
        if board_game[player2_row - 1 ][player2_column - 1 ] == '_ ' :
            board_game[player2_row - 1 ][player2_column - 1] = 'O'
            break
        else : 
            print('(O) This box is not empty! Please Try Again. ')

    show_boardgame(board_game)        