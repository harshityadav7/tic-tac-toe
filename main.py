def print_board(board):
    print("------------")
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2])
        print("-----------")


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # print("draw")
                return False
    return True


def play_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    current_player = 'X'

    while True:
        print_board(board)

        print("player", current_player, "turn")
        row = int(input("enter the row no 0/1/2"))
        col = int(input("enter the col on 0/1/2"))
        if (not 0 <= row <= 2) or (not 0 <= col <= 2):
            continue
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("the space is not vacant")
            continue
        if check_win(board, current_player):
            print_board(board)
            print("player", current_player, "wins")
            break
        if check_draw(board):
            print("draw")
            break
        if current_player == 'X':

            current_player = 'O'
        else:
            current_player = 'X'
play_game()
