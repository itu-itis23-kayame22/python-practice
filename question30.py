import random

words = []

with open('sowpods.txt', 'r') as f:
 line = f.readline().strip()
 words.append(line)
 while line:
    line = f.readline().strip()
    words.append(line)

random_index = random.randint(0, len(words))

print("Random word: ", words[random_index])