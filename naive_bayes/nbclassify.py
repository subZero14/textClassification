classes = {}
dictA = {}
output = "nb.out"
model = "nb_model"
dictsFromFile = []

with open(model, 'r') as f:
	for line in f:
		dictsFromFile.append(eval(line))

if len(dictsFromFile) > 0:
	dictA = dictsFromFile[0]
	classes = dictsFromFile[1]

print dictA
print classes