def letter_queue(commands):
	stack=[]
	for e in commands:
		a=e.split()
		if a[0]=='PUSH': stack.append(a[1])
		elif len(stack): stack.pop(0)
	return ''.join(stack)

if __name__ == '__main__':
	assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
	assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
	assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
	assert letter_queue([]) == "", "Nothing"