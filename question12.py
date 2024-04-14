def extract(elements):

    return [elements[0], elements[-1]]

def main():
    a = [5, 10, 15, 20, 25]
    result_list = extract(a)
    
    
    print("Original list:", a)
    print("New list:", result_list)

main()
