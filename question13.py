def generate(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]  

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def main():
    
    count = int(input("How many Fibonacci numbers would you like? "))  
    fibonacci_numbers = generate(count)
        
    print(fibonacci_numbers)
   

main()