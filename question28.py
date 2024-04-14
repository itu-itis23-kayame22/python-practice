def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = find_max(5, 10, 3)
print("The largest number is:", result)