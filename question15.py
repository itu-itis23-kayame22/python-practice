x = input("Enter a sentence: ")

def reverse(x):
  y = x.split()
  y.reverse()
  return " ".join(y)

a = reverse(x=x)
print(a)