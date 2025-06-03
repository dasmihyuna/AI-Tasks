import math

# Board setup
board = [" " for _ in range(9)]  # 3x3 board (flat list)

# Helper to print the board
def print_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def check_winner(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combos:
        if all(b[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw(b):
    return all(cell != " " for cell in b)

# Get available moves
def get_available_moves(b):
    return [i for i, cell in enumerate(b) if cell == " "]

# Minimax with alpha-beta pruning
def minimax(b, depth, is_maximizing, alpha, beta):
    if check_winner(b, "O"):
        return 10 - depth
    elif check_winner(b, "X"):
        return depth - 10
    elif is_draw(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(b):
            b[move] = "O"
            eval = minimax(b, depth + 1, False, alpha, beta)
            b[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(b):
            b[move] = "X"
            eval = minimax(b, depth + 1, True, alpha, beta)
            b[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI chooses best move
def best_move():
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = "O"
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = "O"

# Main game loop
def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O. Enter positions 1-9 as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")

    while True:
        print_board()

        # Human move
        move = int(input("Your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        if check_winner(board, "X"):
            print_board()
            print("You win... wait, how?!")
            break
        if is_draw(board):
            print_board()
            print("It's a draw!")
            break

        # AI move
        best_move()

        if check_winner(board, "O"):
            print_board()
            print("AI wins. As expected.")
            break
        if is_draw(board):
            print_board()
            print("It's a draw!")
            break

if __name__ == "__main__":
    play()
