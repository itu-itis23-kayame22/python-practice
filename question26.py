def tic_tac_toe(game):
    
    for row in game:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return f"Player {row[0]} wins!"

    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and game[0][col] != 0:
            return f"Player {game[0][col]} wins!"

    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
        return f"Player {game[0][0]} wins!"
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != 0:
        return f"Player {game[0][2]} wins!"

    return "No winner yet."

game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

print(tic_tac_toe(game))