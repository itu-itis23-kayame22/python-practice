import random

def generate_number():
    number = random.sample(range(0, 10), 4)
    return ''.join(str(digit) for digit in number)

def cows_and_bulls(computer_number, user_guess):
    cows = sum(1 for i in range(4) if computer_number[i] == user_guess[i])
    bulls = sum(1 for i in range(4) if user_guess[i] in computer_number and user_guess[i] != computer_number[i])
    return cows, bulls

def main():
    computer_number = generate_number()
    
    while True:
        user_guess = input("Enter your guess: ")
        
        cows, bulls = cows_and_bulls(computer_number, user_guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the right number ")
            break
        
        print(f"{cows} Cows, {bulls} Bulls.")
    
    print("Game Over.")

if __name__ == "__main__":
    main()