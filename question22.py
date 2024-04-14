counter = {}
with open('names.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter:
			counter[line] += 1
		else:
			counter[line] = 1
		line = f.readline()

print(counter)
