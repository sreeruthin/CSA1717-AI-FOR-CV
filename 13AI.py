import math

def minimax(board, depth, maximizing_player, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in get_possible_moves(board):
            board[move] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_possible_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def best_move(board):
    best_value = -math.inf
    move = None
    for (i, j) in get_possible_moves(board):
        board[i][j] = "O"
        move_value = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = " "
        if move_value > best_value:
            best_value = move_value
            move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        if is_full(board) or check_winner(board):
            break
        row, col = map(int, input("Player X, enter row and column: ").split())
        if board[row][col] != " ":
            print("Cell already taken, try again!")
            continue
        board[row][col] = "X"
        if check_winner(board):
            print_board(board)
            print("Player X wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        move = best_move(board)
        board[move[0]][move[1]] = "O"
        if check_winner(board):
            print_board(board)
            print("Player O wins!")
            break

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

play_game()
