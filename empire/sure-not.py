def sure_not(line):return ('' if line[0:4]=='not ' else 'not ')+line

if __name__ == '__main__':
	assert sure_not("sure") == "not sure", "1st example";
	assert sure_not("not sure") == "not sure", "2st example";
	assert sure_not("noter") == "not noter", "3st example";
	print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")