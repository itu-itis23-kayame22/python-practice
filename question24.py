def draw_game_board(size):

    horizontal = " ---"
    vertical = "|   "
    
    for i in range(size):
        print(horizontal * size) 
        print(vertical * (size + 1)) 
    print(horizontal * size) 


if __name__ == "__main__":
    size = int(input("Enter the size of the game board: "))
    
    draw_game_board(size)