def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
        print("-" * 7) 

def get_player_input(symbol, board):
    while True:
        try:
            row = int(input(f"Enter the row (0-2) where you would like to place your {symbol}: "))
            col = int(input(f"Enter the column (0-2) where you would like to place your {symbol}: "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken. Choose another spot.")
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Please enter numbers only.")

def play_tic_tac_toe():
    board = initialize_board()
    print_board(board)
    
    current_symbol = "X"  
    turns = 0
    
    while turns < 9:
        row, col = get_player_input(current_symbol, board)
        board[row][col] = current_symbol
        print_board(board)
        
        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"

        turns += 1
    
    print("Game over, either a win or a draw.")

play_tic_tac_toe()