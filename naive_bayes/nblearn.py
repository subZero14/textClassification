classes = {}
dictA = {}

# Adding a test comment
with open("training.set", 'r') as f:
	file_contents = f.read()	

file_contents = file_contents.split("\n")

for line in file_contents:
	line = line.split(" ")
	currentClass = line[0]
	if currentClass not in classes:
		classes[currentClass] = {}
		classes[currentClass]["wc"] = 0
		classes[currentClass]["cc"] = 0
	classes[currentClass]["wc"] += (len(line) - 1)
	classes[currentClass]["cc"] += 1
	for word in line[1:]:
		if word not in dictA.keys():
			dictA[word] = {} 
		if currentClass not in dictA[word].keys():
			 dictA[word][currentClass] = 0
		dictA[word][currentClass] += 1 

vocabSize = len(dictA.keys())
pClasses = len(file_contents)
for c in classes:
	classes[c]["pC"] = (float)(classes[c]["cc"]) / (float)(pClasses)

print ("pClassesDen:" , pClasses, "\n")
print ("Dict A \n")
print dictA
print ("ClassDict \n")
print classes

#write to model file.
