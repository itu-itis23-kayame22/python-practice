def draw_game_board(width, height):
    horizontal = " ---"
    vertical = "|   "
    
    for i in range(height):
        print(horizontal * width)
        print(vertical * (width + 1))
    print(horizontal * width) 

if __name__ == "__main__":
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    
    draw_game_board(width, height)
