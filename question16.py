import random

letters = ["a", "b", "x", "s", "q", "y", "j", "k", "d", "m", "p", "f"]
symbols = ["@", "?", "/", ",", "<", "&", "%", "#", "*"]
numbers = list(range(1, 101))

def generate_password():
    password = []
    
    initial_letter = random.choice(letters)
    if random.choice([True, False]):
        initial_letter = initial_letter.upper()
    password.append(initial_letter)

    password.append(random.choice(symbols))
    password.append(str(random.choice(numbers)))

    number_of_extra_chars = random.randint(4, 8)
    for _ in range(number_of_extra_chars):
        random_category = random.choice([letters, symbols, numbers])
        random_element = random.choice(random_category)
        if random_category == letters and random.choice([True, False]):  
            random_element = random_element.upper()
        elif random_category == numbers:
            random_element = str(random_element)
        
        password.append(random_element)
    
    random.shuffle(password)
    
    password = ''.join(password)
    return password

password = generate_password()
print("Generated Password:", password)