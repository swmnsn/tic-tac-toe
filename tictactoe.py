# Samantha Kostelni

# prompts the user for their move and updates it in the tic tac toe board
def move():
    move = input("where would you like to play? enter as coordinates with the top left as 0,0 and top middle as 0,1")
    arr = move.split(",")
    row = int(arr[0])
    column = int(arr[1])
    if(row > 2 or column > 2 or row < 0 or column < 0):
        print("this is not a valid move")
    board[row][column] = 'o'
    return row, column

# redraws the board filling in any new changes
def draw_board():
    draw_board = board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "\n" + "---------\n" + board[1][0] + " | " + \
                 board[1][1] + " | " + board[1][2] + "\n" + "---------\n" + board[2][0] + " | " + board[2][1] + " | " + \
                 board[2][2] + "\n"
    print(draw_board)

board = [["x", " ", " "],[" ", " ", " "],[" ", " ", " "]]

#initialize
print("Welcome to tic tac toe!")
draw_board()
row, column = move()

# this is where the computer makes its move based on what your move was, following the perfect tic tac toe chart
if(row == 0 and column == 1):
    board[1][1] = "x"
    draw_board()
    row, column = move()
    if (row == 2 and column ==2):
        board[2][0] = "x"
        draw_board()
        row, column = move()
        if(row == 0 and column == 1):
            board[0][2] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][0] = 'x'
            draw_board()
            print("you lose")
    else:
        board[2][2] = "x"
        draw_board()
        print("you lose")

elif(row == 0 and column == 2):
    board[0][2] = "x"
    draw_board()
    row, column = move()
    if(row == 1 and column == 0):
        board[2][2]= 'x'
        draw_board()
        row, column = move()
        if(row ==1 and column ==1):
            board[2][1] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][1] = 'x'
            draw_board()
            print("you lose")
    else:
        board[1][0] = 'x'
        draw_board()
        print("you lose")

elif(row == 1 and column == 0):
    board[1][1] = "x"
    draw_board()
    row, column= move()
    if(row == 2 and column == 2):
        board[0][2] = 'x'
        draw_board()
        row, column = move()
        if(row == 0 and column == 1):
            board[2][0] = 'x'
            draw_board()
            print("you lose")
        else:
            board[0][1] = 'x'
            draw_board()
            print("you lose")
    else:
        board[2][2] = 'x'
        draw_board()
        print("you lose")

elif(row == 1 and column == 1):
    board[2][2] = "x"
    draw_board()
    row, column= move()
    if(row == 0 and column == 1):
        board[2][1] = 'x'
        draw_board()
        row, column = move()
        if(row ==2 and column == 0):
            board[0][2]= 'x'
            draw_board()
            row, column = move()
            if(row == 1 and column == 0):
                board[1][2] = 'x'
                draw_board()
                print("you lose")
            else:
                board[1][0] = 'x'
                draw_board()
                print("it's a tie!")
        else:
            board[2][1] = 'x'
            draw_board()
            print("you lose")

    elif (row == 0 and column == 2):
        board[2][0] = 'x'
        draw_board()
        row, column = move()
        if(row == 1 and column == 0):
            board[2][1] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][0] = 'x'
            draw_board()
            print("you lose")

    elif(row == 1 and column == 0):
        board[1][2] = 'x'
        draw_board()
        row, column = move()
        if(row == 0 and column ==2):
            board[2][0] = 'x'
            draw_board()
            row, column = move()
            if(row == 0 and column == 1):
                board[2][1] = 'x'
                draw_board()
                print("you lose")
            else:
                board[0][1] = 'x'
                draw_board()
                print("it's a draw")

        else:
            board[0][2] = 'x'
            draw_board()
            print("you lose")

    elif(row == 1 and column ==2):
        board[1][0] ='x'
        draw_board()
        row, column = move()
        if(row == 2 and column == 0):
            board[0][2] = 'x'
            draw_board()
            row, column = move()
            if(row == 0 and column == 2):
                board[2][1] = 'x'
                draw_board()
                print("it's a draw")
            else:
                board[0][2] = 'x'
                draw_board()
                print("you lose")
        else:
            board[2][0] = 'x'
            draw_board()
            print("you lose")

    elif(row ==2 and column == 0):
        board[0][2] = 'x'
        draw_board()
        row, column = move()
        if(row == 0 and column ==1 ):
            board[1][2] = 'x'
            draw_board()
            print("you lose")
        else:
            board[0][1] = 'x'
            draw_board()
            print("you lose")

    elif (row == 2 and column == 1):
        board[0][1] = 'x'
        draw_board()
        row, column = move()
        if(row == 0 and column == 2):
            board[2][0] = 'x'
            draw_board()
            row, column = move()
            if(row == 1 and column == 0):
                board[1][2] = 'x'
                draw_board()
                print("it's a draw")
            else:
                board[1][0] = 'x'
                draw_board()
                print("you lose")
        else:
            board[0][2] = 'x'
            draw_board()
            print("you lose")

elif(row == 1 and column == 2):
    board[1][1] = "x"
    draw_board()
    row, column= move()
    if(row == 2 and column == 2):
        board[0][2] = 'x'
        draw_board()
        row, column = move()
        if(row == 0 and column ==1):
            board[2][0] = 'x'
            draw_board()
            print("you lose")
        else:
            board[0][1] = 'x'
            draw_board()
            print("you lose")
    else:
        board[2][2] = 'x'
        draw_board()
        print("you lose")

elif(row == 2 and column == 0):
    board[0][2] = "x"
    draw_board()
    row, column= move()
    if( row == 0 and column == 1):
        board[2][2] = 'x'
        draw_board()
        row, column = move()
        if(row == 1 and column == 2):
            board[1][1] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][2] = 'x'
            draw_board()
            print("you lose")
    else:
        board[0][1]= 'x'
        print("you lose")

elif(row == 2 and column == 1):
    board[1][1] = "x"
    draw_board()
    row, column= move()
    if(row ==2 and column ==2):
        board[2][0] = 'x'
        draw_board()
        row, column = move()
        if(row == 1 and column == 0):
            board[1][1] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][0] = 'x'
            draw_board()
            print("you lose")
    else:
        board[2][2] = 'x'
        draw_board()
        print("you lose")

elif(row == 2 and column == 2):
    board[0][2] = "x"
    draw_board()
    row, column= move()
    if(row == 0 and column == 1):
        board[2][1] = 'x'
        draw_board()
        row, column = move()
        if(row == 1 and column == 0):
            board[1][1] = 'x'
            draw_board()
            print("you lose")
        else:
            board[1][0] = 'x'
            draw_board()
            print("you lose")
    else:
        board[0][1] = 'x'
        draw_board()
        print("you lose")

else:
    print("this is not a valid move")
