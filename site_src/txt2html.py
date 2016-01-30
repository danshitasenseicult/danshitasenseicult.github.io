inputfile = open("danshitatext.txt", 'r')
outputfile = open("outputfile.txt", 'w')

lines =  inputfile.readlines()

for x in range(0, len(lines)):
	outputfile.write("<p>" + lines[x][:-2] + "<p/>\n")


inputfile.close()
outputfile.close()
