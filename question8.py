
user1 = input("player1 name? ")
user2 = input("player2 name? ")
choice1 = input("player1 choice: ")
choice2 = input("player2 choice: ")

def winner(choice1, choice2):
    
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'scissors' and choice2 == 'paper') or \
         (choice1 == 'paper' and choice2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def rock_paper_scissors():
    
    result = winner(choice1, choice2)
    print(result)
        
        
rock_paper_scissors()