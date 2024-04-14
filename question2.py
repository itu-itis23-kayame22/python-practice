num = int(input("Enter a number; "))
left = num%2

match(left):
    case 0:
        print("You have entered an even number")
    case 1:
        print("You have entered an odd number")
