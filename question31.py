def hangman_game():
    word = "LEGOLAS"
    guessed = ["_" for _ in word]  
    guessed_letters = set()  
    word_complete = False

    print("Welcome to Hangman!")
    print(" ".join(guessed))  

    while not word_complete:
        guess = input("Guess your letter: ").upper()
        
        if guess in word:
            
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            
            guessed_letters.add(guess)
            
            if "_" not in guessed:
                word_complete = True
            print(" ".join(guessed))
        else:
            print("Incorrect!")
            guessed_letters.add(guess)  

        print("Guessed so far: ", " ".join(sorted(guessed_letters)))

    print("You found")

hangman_game()