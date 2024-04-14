my_string = input("Enter a word; ")
x = 0
y=0
list_of_characters = list(my_string)
length = len(list_of_characters)


while x<=length:
    if list_of_characters[x] != list_of_characters[length-1]:
        y+=1
    x+=1
    length-=1

if y==0:
    print("it's a palindrome word") 
else:
    print("it's not a palindrome word")



