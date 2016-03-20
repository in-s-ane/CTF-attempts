with open('EZ.txt') as f:
	data = f.read()
	string = ""
	for symbol in data:
		if symbol == ' ':
			string += " "
		elif symbol == '&':
			string += "-"
		elif symbol == '!':
			string += "."
		
print string
