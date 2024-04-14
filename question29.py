def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    lines = board + [list(x) for x in zip(*board)]  
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]  
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != ' ':
            return line[0]
    return None

def make_move(board, position, player):
    row, col = divmod(position - 1, 3)
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def get_free_positions(board):
    return [i + 1 for i in range(9) if board[i // 3][i % 3] == ' ']

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        free_positions = get_free_positions(board)
        if not free_positions:
            print("It's a draw!")
            break
        
        print(f"Player {current_player}, choose from these positions: {free_positions}")
        position = int(input("Enter your move (1-9): "))
        if position not in free_positions:
            print("Invalid move, try again.")
            continue
        
        make_move(board, position, current_player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()