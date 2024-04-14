import json

def load_birthdays(filename):

    with open(filename, 'r') as f:
        birthdays = json.load(f)
    return birthdays
    

def main():
    birthday_dictionary = load_birthdays("birthdays.json")

    
    name = input("Whose birthday do you want to look up? Type 'quit' to exit. ")
    if name in birthday_dictionary:
         print(f"{name}'s birthday is on {birthday_dictionary[name]}")
    else:
        print(f"Sorry, there is no data for {name}.")


main()