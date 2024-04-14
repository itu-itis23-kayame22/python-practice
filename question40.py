import random

number = random.randint(1, 9)
guesses = 0
while True:
	while True:
		try:
			guess = int(input("Guess a number between 1 and 9: "))
			if guess >= 1 and guess <= 9:
				break
			else:
				print("Your input must be a number between 1 and 9 inclusive")
		except ValueError:
			print("You must enter a number")
	guesses += 1
	if guess == number:
		break
print(f"You found in {guesses} try")