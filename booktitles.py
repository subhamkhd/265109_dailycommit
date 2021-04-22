file = open("/usercode/files/books.txt", "r")

#your code goes here
fileLines = []
for lines in file:
	fileLines.append(lines)
length = 1
for n in fileLines:
	if length == len(fileLines):
		print(n[0] + str(len(n)))
	else:
		print(n[0] + str(len(n)-1))
	length += 1
file.close()