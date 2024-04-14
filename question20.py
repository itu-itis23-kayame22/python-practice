def find(list, element):
  for i in list:
    if i == element:
      return True
  return False
  
if __name__=="__main__":
  list = [2, 4, 6, 8, 10]
  x = int(input("enter a number to check: "))
  print(find(list, x)) 
