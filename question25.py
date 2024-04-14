def guess_number():
    low = 0
    high = 100
    guesses = 0
    print("Guess a number between 0 and 100")

    while low <= high:
        guess = (low + high) // 2
        print(f"My guess is {guess}.")
        feedback = input("Enter 'high', 'low', or 'correct': ").lower().strip()
        
        guesses += 1
        if feedback == 'correct':
            print(f"I guessed the number in {guesses} guesses!")
            break
        elif feedback == 'high':
            low = guess 
        elif feedback == 'low':
            high = guess 

guess_number()