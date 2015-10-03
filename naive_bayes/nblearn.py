import sys, getopt, json

classes = {}
dictA = {}
inputfile = "training.set"
outputfile = "nb_model"

def train():
	# Adding a test comment
	with open(inputfile, 'r') as f:
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

	#write to model file.
	with open(outputfile, 'w') as fp:
		fp.write(str(dictA) + "\n")
		# fp.write("\n")
		fp.write(str(classes))
		# json.dump(classes, fp)
		# json.dump(dictA, fp)

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'nblearn.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'nblearn.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   # print 'Input file is "', inputfile
   # print 'Output file is "', outputfile
   print("Training..")
   train()

if __name__ == "__main__":
   main(sys.argv[1:])
