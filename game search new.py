import numpy as np

# Function to check if the board is full
def is_board_full(board):
    return not any(' ' in row for row in board)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the current board state
def evaluate_board(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using the minimax algorithm
def find_best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to print the current board state
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to play the Tic-Tac-Toe game
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while not is_board_full(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
        # Player's move
        row, col = map(int, input("Enter your move (row and column separated by space): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'O'
            print_board(board)
        else:
            print("Invalid move! Try again.")
            continue
        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            return
        elif is_board_full(board):
            print("It's a draw!")
            return

        # Computer's move
        print("Computer's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Computer wins!")
            return
        elif is_board_full(board):
            print("It's a draw!")
            return

# Play the game
play_tic_tac_toe()
