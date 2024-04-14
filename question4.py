num = int(input("Enter a number to divide: "))
div_List = []
x = 1

while x<=num:
    if num % x == 0:
        div_List.append(x)
    x+= 1

print(div_List)